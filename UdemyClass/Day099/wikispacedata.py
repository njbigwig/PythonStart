import re
import time
import warnings
from typing import List, Optional

import pandas as pd
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=UserWarning)

# -----------------------------
# Configuration
# -----------------------------
DECADE_URLS = {
    "1951-1960": "https://en.wikipedia.org/wiki/Timeline_of_spaceflight_1951–1960",
    "1961-1970": "https://en.wikipedia.org/wiki/Timeline_of_spaceflight_1961–1970",
    "1971-1980": "https://en.wikipedia.org/wiki/Timeline_of_spaceflight_1971–1980",
    "1981-1990": "https://en.wikipedia.org/wiki/Timeline_of_spaceflight_1981–1990",
    "1991-2000": "https://en.wikipedia.org/wiki/Timeline_of_spaceflight_1991–2000",
    "2001-2010": "https://en.wikipedia.org/wiki/Timeline_of_spaceflight_2001–2010",
    "2011-2020": "https://en.wikipedia.org/wiki/Timeline_of_spaceflight_2011–2020",
    "2021-2030": "https://en.wikipedia.org/wiki/Timeline_of_spaceflight_2021–2030",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

RETRY_ATTEMPTS = 3
RETRY_DELAY = 1.5

OUTPUT_CSV = "all_space_missions.csv"


# -----------------------------
# Helpers
# -----------------------------
def fetch_html(url: str) -> Optional[str]:
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=20)
            if resp.status_code == 200:
                return resp.text
            print(f"HTTP {resp.status_code} for {url} (attempt {attempt}/{RETRY_ATTEMPTS})")
        except requests.RequestException as e:
            print(f"Request error for {url}: {e} (attempt {attempt}/{RETRY_ATTEMPTS})")
        time.sleep(RETRY_DELAY)
    return None


def column_name_map(col: str) -> str:
    """Normalize column names to facilitate matching across years."""
    c = str(col).strip().lower()
    c = re.sub(r"\s+", " ", c)
    return c


def has_launch_like_columns(df: pd.DataFrame) -> bool:
    cols = [column_name_map(c) for c in df.columns]
    signals = [
        any(k in cols for k in ["date", "launch date", "time", "launch"]),
        any(k in cols for k in ["payload", "mission", "object", "satellite", "spacecraft"]),
        any(k in cols for k in ["rocket", "launch vehicle", "carrier rocket"]),
    ]
    return sum(signals) >= 2


def extract_first_nonempty(df: pd.DataFrame, candidates: List[str]) -> Optional[pd.Series]:
    cols = {column_name_map(c): c for c in df.columns}
    for cand in candidates:
        if cand in cols:
            return df[cols[cand]]
    return None


import re
import pandas as pd

def clean_text(val):
    if pd.isna(val):
        return None
    # Remove reference markers like [1], [23], etc.
    txt = re.sub(r"\[\d+\]", "", str(val))
    # Collapse multiple spaces into one and strip leading/trailing whitespace
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt if txt else None




def parse_date_to_datetime(date_str: Optional[str]) -> pd.Timestamp:
    if date_str is None:
        return pd.NaT
    s = date_str
    # Remove parenthetical timezones or notes
    s = re.sub(r"\(.*?\)", "", s)
    s = s.replace("~", " ").replace("≈", " ").strip()
    # Wikipedia has many formats; let pandas try best effort
    dt = pd.to_datetime(s, errors="coerce", utc=False, infer_datetime_format=True)
    if pd.isna(dt):
        # Try extracting a year and month/day manually
        # Examples: "1969-07-16", "12 April 1961", "April 1961"
        # If only year present, fallback to Jan 1
        year_match = re.search(r"(\d{4})", s)
        if year_match:
            y = int(year_match.group(1))
            # Try month/day words
            month_match = re.search(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)", s, re.I)
            day_match = re.search(r"\b(\d{1,2})\b", s)
            m = 1
            d = 1
            if month_match:
                months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
                m = months.index(month_match.group(1).lower()) + 1
            if day_match:
                d = int(day_match.group(1))
            try:
                dt = pd.Timestamp(year=y, month=m, day=d)
            except Exception:
                dt = pd.NaT
    return dt


def normalize_outcome(outcome: Optional[str]) -> Optional[str]:
    if outcome is None:
        return None
    o = outcome.lower()
    if any(w in o for w in ["success", "successful", "operational", "partial success"]):
        # Distinguish partial success
        if "partial" in o:
            return "Partial Failure"
        return "Success"
    if any(w in o for w in ["failure", "failed", "launch failure", "catastrophic", "loss"]):
        return "Failure"
    if any(w in o for w in ["partial", "anomaly", "underperformed"]):
        return "Partial Failure"
    return None


def extract_country(operator: Optional[str], location: Optional[str]) -> Optional[str]:
    # Heuristic: try operator first, then last token of location after comma
    if operator:
        # operator examples: "NASA (United States)", "Roscosmos (Russia)"
        m = re.search(r"\(([^)]+)\)", operator)
        if m:
            return clean_text(m.group(1))
        # else try country words
        for candidate in ["United States", "USA", "Russia", "Soviet Union", "China", "France",
                          "Japan", "India", "UK", "United Kingdom", "Israel", "Iran", "South Korea",
                          "North Korea", "New Zealand", "Canada", "Brazil", "Argentina", "Australia"]:
            if candidate.lower() in operator.lower():
                return candidate
    if location:
        parts = [p.strip() for p in location.split(",") if p.strip()]
        if parts:
            # last part often country/state; prefer last two tokens for cases like "Cape Canaveral, Florida, United States"
            last = parts[-1]
            # If last is a state, try previous
            if last in ["Florida", "California", "Texas", "Kazakhstan", "French Guiana"]:
                if len(parts) >= 2:
                    return parts[-1] if parts[-1] not in ["Florida", "California", "Texas"] else parts[-2]
            return last
    return None


# -----------------------------
# Scrape and normalize
# -----------------------------
def scrape_decade(url: str) -> List[pd.DataFrame]:
    html = fetch_html(url)
    if not html:
        print(f"❌ Could not fetch {url}")
        return []

    # Read all tables from the page
    try:
        tables = pd.read_html(html)
    except ValueError:
        print(f"⚠️ No tables detected on {url}")
        return []

    normalized_frames = []

    for t in tables:
        # Quickly skip tables that are obviously unrelated
        if not has_launch_like_columns(t):
            continue

        # Normalize candidate columns
        t_cols_norm = {c: column_name_map(c) for c in t.columns}

        def get_col(cands: List[str]) -> Optional[pd.Series]:
            for cn, raw in t_cols_norm.items():
                # cn is original col, raw is normalized
                pass
            # reverse lookup: normalized -> original
            norm_to_orig = {column_name_map(orig): orig for orig in t.columns}
            for cand in cands:
                if cand in norm_to_orig:
                    return t[norm_to_orig[cand]]
            return None

        date_col = extract_first_nonempty(t, ["date", "launch date", "time", "launch"])
        mission_col = extract_first_nonempty(t, ["payload", "mission", "object", "satellite", "spacecraft"])
        vehicle_col = extract_first_nonempty(t, ["rocket", "launch vehicle", "carrier rocket"])
        location_col = extract_first_nonempty(t, ["launch site", "site", "location"])
        operator_col = extract_first_nonempty(t, ["operator", "agency", "organisation", "organization", "launch provider"])
        outcome_col = extract_first_nonempty(t, ["outcome", "result", "status"])

        # Build normalized dataframe
        n = max(len(t), 0)
        df_out = pd.DataFrame({
            "Date": [None] * n,
            "Mission": [None] * n,
            "Vehicle": [None] * n,
            "Location": [None] * n,
            "Country": [None] * n,
            "Company": [None] * n,
            "Mission_Status": [None] * n,
            "Price": [None] * n,  # Wikipedia doesn't provide price; keep for compatibility
        })

        if date_col is not None:
            df_out["Date"] = [clean_text(v) for v in date_col]
        if mission_col is not None:
            df_out["Mission"] = [clean_text(v) for v in mission_col]
        if vehicle_col is not None:
            df_out["Vehicle"] = [clean_text(v) for v in vehicle_col]
        if location_col is not None:
            df_out["Location"] = [clean_text(v) for v in location_col]
        if operator_col is not None:
            ops = [clean_text(v) for v in operator_col]
            df_out["Company"] = ops
            # Derive Country from Operator or Location
            df_out["Country"] = [
                extract_country(operator=ops[i], location=df_out["Location"].iloc[i])
                for i in range(n)
            ]
        else:
            df_out["Country"] = [
                extract_country(operator=None, location=df_out["Location"].iloc[i])
                for i in range(n)
            ]

        if outcome_col is not None:
            df_out["Mission_Status"] = [normalize_outcome(clean_text(v)) for v in outcome_col]

        # Parse Date -> datetime and Year
        df_out["Date"] = [parse_date_to_datetime(d) for d in df_out["Date"]]
        df_out["Year"] = df_out["Date"].dt.year

        # Keep only rows that have at least Vehicle or Mission and a non-empty Date or Year
        df_out = df_out[
            (df_out["Vehicle"].notna() | df_out["Mission"].notna()) &
            (df_out["Date"].notna() | df_out["Year"].notna())
        ]

        # Deduplicate obvious duplicates
        df_out = df_out.drop_duplicates(subset=["Date", "Mission", "Vehicle", "Location"], keep="first")

        if not df_out.empty:
            normalized_frames.append(df_out)

    return normalized_frames


def main():
    all_frames: List[pd.DataFrame] = []

    for decade, url in DECADE_URLS.items():
        print(f"Scraping decade {decade} -> {url}")
        frames = scrape_decade(url)
        if frames:
            print(f"  ✓ Collected {sum(len(f) for f in frames)} rows from {decade}")
            all_frames.extend(frames)
        else:
            print(f"  ⚠️ No usable tables found for {decade}")

    if not all_frames:
        print("❌ No data scraped at all. Check connectivity or Wikipedia layout changes.")
        return

    df_all = pd.concat(all_frames, ignore_index=True)

    # Final cleaning and enhancements
    # Standardize country names (light touch)
    country_fix = {
        "USA": "United States",
        "U.S.A.": "United States",
        "US": "United States",
        "U.S.": "United States",
        "Soviet Union": "Soviet Union",
        "Russian Federation": "Russia",
        "UK": "United Kingdom",
        "French Guiana": "France",  # spaceport Kourou
    }
    df_all["Country"] = df_all["Country"].apply(lambda x: country_fix.get(x, x) if pd.notna(x) else x)

    # Fill Year if missing from Date
    df_all["Year"] = df_all["Year"].fillna(df_all["Date"].dt.year)

    # Sort by date/year for readability
    df_all = df_all.sort_values(by=["Year", "Date", "Country", "Vehicle"], na_position="last")

    # Reorder columns to match your analysis program
    cols_order = ["Mission", "Date", "Year", "Vehicle", "Location", "Country", "Company", "Mission_Status", "Price"]
    df_all = df_all.reindex(columns=cols_order)

    # Persist
    df_all.to_csv(OUTPUT_CSV, index=False)

    print(f"✅ Saved {OUTPUT_CSV} with {len(df_all)} records")
    # Quick sanity prints
    print("Columns:", list(df_all.columns))
    print("Sample:")
    print(df_all.head(10))


if __name__ == "__main__":
    main()
