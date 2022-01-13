import time
import os
import re
from selenium import webdriver
from config import repo_dir, downloads_dir, webdriver_loc


def download_csv(action_type, start_date, end_date, zipcode, download_repo):
    # this script goes to the action_page type on the portland maps

    # set up formats of stuff well need later
    clean_start_date = start_date.strftime("%m%%2F%d%%2F%Y")
    clean_end_date = end_date.strftime("%m%%2F%d%%2F%Y")
    clean_zipcode = "%25" + str(zipcode) + "%25"
    csv_zipcode = str(zipcode)
    csv_location = download_repo

    # make sure your chromedriver is in the home directory of the repo
    driver = webdriver.Chrome(webdriver_loc)

    # open ted's page no sos and download it.
    driver.maximize_window()
    driver.get("https://www.portlandmaps.com/reports/index.cfm?action=" + action_type +
               "&start_date=" + clean_start_date +
               "&search_date=Date_Received" +
               "&end_date=" + clean_end_date +
               "&search_field=ADDRESS" +
               "&search_value=" + clean_zipcode
               )

    try:
        driver.find_element_by_css_selector('button[value="csv"]').click()
        time.sleep(2)  # sleep just to make sure it can download
        # move csv and rename to search filters
        new_file_name = csv_location + "/" + action_type + csv_zipcode + ".csv"
        print(new_file_name)
        os.rename(downloads_dir + action_type + '-report.csv', new_file_name)
    except Exception as ex:
        print(ex)
        print("no results")

    driver.close()
