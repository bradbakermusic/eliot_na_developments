action_types = [
    "accessory-dwelling-unit",
    "short-term-rental",
    "co-intakes",
    "co-issued",
    "fp-issued",
    "fp-intakes",
    "lur-intakes",
    "rs-issued",
    "rs-intakes",
]

action_types_to_readable = {
    "accessory-dwelling-unit": "Accessory Dwelling Unit",
    "short-term-rental": "Short Term Rental",
    "co-intakes": "Commercial Building Permit Intakes",
    "co-issued": "Commercial Issued Building Permits",
    "fp-issued": "Facility Issued Permits",
    "fp-intakes": "Facility Permit Intakes",
    "lur-intakes": "Land Use Review Intakes",
    "rs-issued": "Residential Issued Building Permits",
    "rs-intakes": "Residential Permit Intakes",
}

zipcodes = [97212, 97227]

addresses = {
    "ne_ns": {
        "streets": [
            "NE VICTORIA AVE",
            "NE 1ST AVE",
            "NE RODNEY AVE",
            "NE 2ND AVE",
            "NE 3RD AVE",
            "NE MARTIN LUTHER KING BLVD",
            "NE GRAND AVE",
            "NE 7TH AVE",
        ],
        "min_adresses": 1700,
        "max_address": 3500,
    },
    'ne_ew': {
        "streets": [
            "NE BROADWAY",
            "NE Schuyler ST",
            "NE HANCOCK ST",
            "NE SAN RAFAEL ST",
            "NE TILLAMOOK ST",
            "NE THOMPSON ST",
            "NE SACRAMENTO ST",
            "NE RUSSELL ST",
            "NE KNOTT ST",
            "NE GRAHAM ST",
            "NE STANTON ST",
            "NE MORRIS ST",
            "NE MONROE ST",
            "NE FARGO ST",
            "NE COOK ST",
            "NE IVY ST",
            "NE FREMONT ST",
        ],
        "min_adresses": 0,
        "max_address": 700,
    },
    'n_ns': {
        "streets": [
            "N WILLIAMS AVE",
            "N VANCOUVER AVE",
            "N GANTENBEIN AVE",
            "N COMMERCIAL AVE",
            "N KERBY AVE",
            "N FLINT AVE",
            "N WHEELER AVE"

        ],
        "min_adresses": 1700,
        "max_address": 3500,
    },
    'n_ew': {
        "streets": [
            "N BROADWAY",
            "N SCHUYLER ST",
            "N HANCOCK ST",
            "N SAN RAFAEL ST",
            "N TILLAMOOK ST",
            "N THOMPSON ST",
            "N PAGE ST"
            "N SACRAMENTO ST",
            "N RUSSELL ST",
            "N KNOTT ST",
            "N GRAHAM ST",
            "N STANTON ST",
            "N MORRIS ST",
            "N MONROE ST",
            "N FARGO ST",
            "N COOK ST",
            "N IVY ST",
            "N FREMONT ST",
            "N DIXON ST",
            "N RIVER ST",
            "N LORING ST",
            "N RAILROAD ST"

        ],
        "min_adresses": 0,
        "max_address": 2000,
    },
    'albina_ns': {
        "streets": [
            "N ROSS AVE",
            "N BORTHWICK AVE",
            "N ALBINA AVE",
            "N INTERSTATE AVE",
            "N MISSISSIPPI AVE",
            "N INTERSTATE AVE",
            "N CLARK AVE",
            "N LEWIS AVE",
            "N HARDING AVE",
            "N RANDOLPH AVE"
            "N NESMITH AVE",
            "N LARRABEE AVE",
            "N BENTON AVE",
            "N ROSS AVE",
            "N WHEELER AVE",
        ],
        "min_adresses": 800,
        "max_address": 1799,
    }
}
