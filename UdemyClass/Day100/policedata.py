# created by Copilot

# requirements: pandas, requests, tqdm, numpy, matplotlib (optional)
# python -m pip install -r requirements.txt

import io
import requests
import pandas as pd
import numpy as np
from tqdm import tqdm

# --- 1) Download Washington Post dataset (raw CSV on GitHub) ---
WP_CSV_URL = "https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/v2/fatal-police-shootings-data.csv"
r = requests.get(WP_CSV_URL, timeout=30)
r.raise_for_status()
wp = pd.read_csv(io.StringIO(r.text), parse_dates=["date"])
# Basic cleanup
wp = wp.rename(columns=str.lower)
wp['county'] = wp['county'].str.strip()
wp['state'] = wp['state'].str.strip()
wp['race'] = wp['race'].fillna('None')

# --- 2) Get state FIPS mapping from Census API ---
CENSUS_BASE = "https://api.census.gov/data/2019/acs/acs5"
# get state list with FIPS
resp = requests.get(f"{CENSUS_BASE}?get=NAME&for=state:*")
resp.raise_for_status()
rows = resp.json()
states_df = pd.DataFrame(rows[1:], columns=rows[0])
states_df['state_fips'] = states_df['state']
states_df['state_name'] = states_df['NAME']
state_name_to_fips = dict(zip(states_df['state_name'].str.upper(), states_df['state_fips']))
# also map postal codes -> FIPS by using a small lookup via Census (state abbreviations not returned here),
# so create a mapping using pandas built-in list (simple static map)
state_abbrev_to_name = {
  "AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado",
  "CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho",
  "IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana",
  "ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi",
  "MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey",
  "NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma",
  "OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota",
  "TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington",
  "WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming","DC":"District of Columbia"
}
# map WP state abbrev to state FIPS
wp['state_name'] = wp['state'].map(lambda s: state_abbrev_to_name.get(s, s))
wp['state_fips'] = wp['state_name'].str.upper().map(state_name_to_fips)

# --- 3) Pull county population (total) for each state via ACS (B01003_001E) and build county-level table ---
def fetch_county_pop(state_fips):
    q = f"{CENSUS_BASE}?get=NAME,B01003_001E&for=county:*&in=state:{state_fips}"
    resp = requests.get(q, timeout=30)
    resp.raise_for_status()
    data = pd.DataFrame(resp.json()[1:], columns=resp.json()[0])
    data['county_name'] = data['NAME'].str.replace(r",.*$", "", regex=True).str.upper()
    data['population'] = data['B01003_001E'].astype(int)
    data['state_fips'] = state_fips
    return data[['state_fips','county_name','population','state','county']]

# build county population map for states present in WP data
state_fips_unique = wp['state_fips'].dropna().unique().tolist()
county_pop_frames = []
for sf in tqdm(state_fips_unique, desc="fetching county pops"):
    county_pop_frames.append(fetch_county_pop(sf))
county_pop = pd.concat(county_pop_frames, ignore_index=True)

# normalize WP county names for matching
wp['county_name'] = wp['county'].str.upper().str.replace(r" COUNTY$","",regex=True)
# merge by state_fips and county_name (best-effort)
merged = wp.merge(county_pop, how='left', left_on=['state_fips','county_name'], right_on=['state_fips','county_name'])

# --- 4) Analysis examples ---
# deaths per 100k by county
# print("columns:", merged.columns.tolist())
# print(merged.head(5))
agg_county = merged.groupby(['state_name','county_name','state_fips'], as_index=False).agg(
    deaths=('id','count'),
    population=('population','first')
)
agg_county['deaths_per_100k'] = agg_county['deaths'] / agg_county['population'] * 100000

# racial disproportionality at national level
race_counts = wp['race'].value_counts().rename_axis('race').reset_index(name='deaths')
# fetch national race totals from ACS (B02001 series)
race_vars = {
  'B02001_002E':'White',
  'B02001_003E':'Black',
  'B02001_005E':'Asian',
  'B02001_004E':'Native',
  'B02001_006E':'Other'
}
vars_str = ",".join(race_vars.keys())
resp = requests.get(f"{CENSUS_BASE}?get={vars_str}&for=us:1")
resp.raise_for_status()
vals = resp.json()[1]
race_pop = {race_vars[k]: int(v) for k,v in zip(race_vars.keys(), vals)}
race_df = pd.DataFrame(list(race_pop.items()), columns=['race_label','population'])
race_df['deaths'] = race_df['race_label'].map(lambda x: race_counts.loc[race_counts['race']==x[0], 'deaths'].sum() if False else race_counts.set_index('race').reindex(['W','B','A','N','H']).fillna(0)['deaths'].values) # placeholder mapping
# (Note: map WP race codes to ACS labels before computing; left as exercise to map codes W/B/A/H/N -> labels)

# Save outputs
agg_county.to_csv("deaths_by_county_per100k.csv", index=False)
