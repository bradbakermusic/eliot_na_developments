from datetime import date, timedelta
from sys import exit
import os
import glob
import re
import pandas as pd
import tweepy
from config import repo_dir, downloads_dir
from config import api_key, api_key_secret, bearer_token, access_token, \
    access_token_secret
from constants import zipcodes, addresses, action_types, \
    action_types_to_readable
from functions import download_csv

# assuming this will be run every monday
ds = date.today() - timedelta(days=1)
ds_week_ago = ds - timedelta(days=7)
tmp_file_repo = repo_dir + "/tmp" + ds.strftime("%Y%m%d")
os.mkdir(tmp_file_repo)

# download all report types
for action_type in action_types:
    # remove any files of the same name in the downloads folder
    for filename in glob.glob(downloads_dir + action_type + "*"):
        os.remove(filename)
    for zipcode in zipcodes:
        download_csv(
            action_type,
            ds_week_ago,
            ds,
            zipcode,
            tmp_file_repo
            )

# allow full display of strings
pd.options.display.max_colwidth = 9999

# set up twitter client
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token)


# iterate through all the files
for filename in os.listdir(tmp_file_repo):
    df = pd.read_csv(tmp_file_repo + '/' + filename, index_col=False)
    # extract street name and address number
    df['address_num'] = df['ADDRESS'].str.extract(r'([0-9]+)')
    df['street_name'] = df['ADDRESS'].str.extract(r' ([A-Z0-9 ]+)')
    # loop through all the addresses in the constants file
    for addr_group in addresses:
        # filter
        trimmed_df = df[df['street_name'].isin(addresses[addr_group]['streets'])]
        trimmed_df = trimmed_df[trimmed_df['address_num'].astype(int) >= addresses[addr_group]['min_adresses']]
        trimmed_df = trimmed_df[trimmed_df['address_num'].astype(int) <= addresses[addr_group]['max_address']]
        # if there are any results, loop through the rows
        if trimmed_df.shape[0] > 0:
            for index, row in trimmed_df.iterrows():
                try:
                    # first tweet stuff
                    first_tweet_content = """Report Type: {0}
Address: {1}
Date: {2}
                    """.format(action_types_to_readable[re.findall(r'([a-z\-]+)', filename)[0]],
                               row['ADDRESS'],
                               row['DATE_RECEIVED'])
                    post_response = client.create_tweet(text=first_tweet_content)
                    posted_tweet_id = post_response.data['id']
                    # second tweet stuff. Reply to the first tweet
                    second_tweet_content = """Description of Work: {0}""".format(row['DESCRIPTION_OF_WORK'][0:139])
                    post_response = client.create_tweet(text=second_tweet_content, in_reply_to_tweet_id=posted_tweet_id)
                    posted_tweet_id = post_response.data['id']
                    # third tweet stuff. Reply to the second tweet
                    third_tweet_content = """Permit Details: {0}""".format(row['PERMIT_DETAILS'])
                    post_response = client.create_tweet(text=third_tweet_content, in_reply_to_tweet_id=posted_tweet_id)
                except Exception as ex:
                    print('something bugged')
                    print(ex)
                    print(row)
