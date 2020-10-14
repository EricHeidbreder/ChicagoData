#!/usr/bin/env python

import pandas as pd
from auth import auth
from sodapy import Socrata

# app_token="4n18iMKDZeddcBRHi8wA7NiIy"
# my_access_token="r222EwUUg6JsHm1OGBR5A9Q0rEn_zV5Miwor"

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = auth()

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("qmqz-2xku", 'csv', 
                    select='*', limit=40000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

results_df.to_csv('./data/beach_water_quality_2013-present', index=False, header=results_df.iloc[0].tolist())
