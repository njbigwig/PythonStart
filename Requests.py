# need to install Requests package:
#  pip install requests
# There is a bug in the feed, for the year 2022, the populution has not yet been defined. value = "none".

import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
    if ( year["date"] != "2022" ):
        display_width = year["value"] // 10_000_000
        print(f'{year["date"]}: {year["value"]}', "=" * display_width)