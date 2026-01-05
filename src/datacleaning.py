import pandas as pd
import numpy as np


# Load the messy data
df = pd.read_csv('data/marketing_campaign_data_messy.csv')

print(f"Loaded Dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# ==========================================
#            HEADER CLEANING
# ==========================================
print("ORIGINAL COLUMNS")
print(df.columns.tolist())

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print("FIX APPLIED")
print(df.columns.tolist())

# ==========================================
# STEP 2: TYPE CONVERSION & CURRENCY CLEANING
# ==========================================

dirty_spend_mask = df['spend'].astype(str).str.contains(r'\$')
print(df.loc[dirty_spend_mask,['campaign_id','spend']].head(3))

df['spend'] = df['spend'].astype(str).str.replace(r'[^\d.-]', '', regex=True)
df['spend'] = pd.to_numeric(df['spend'])

print("FIX APPLIED")
print(df.loc[dirty_spend_mask,['campaign_id','spend']].head(3))


# ==========================================
#    CATEGORICAL TYPES
# ==========================================

print(df['channel'].unique())

cleanup_map = {
    'Facebok': 'Facebook',
    'Insta_gram': 'Instagram',
    'Gogle': 'Google Ads',
    'Tik_Tok': 'TikTok',
    'E-mail': 'Email',
    'N/A': np.nan  # Handling the ghost value here too
}

df['channel'] = df['channel'].replace(cleanup_map)

print("FIX APPLIED")
print(df['channel'].unique())


# ==========================================
#        HANDLING MIXED BOOLEANS
# ==========================================

print(df['active'].unique())

bool_map = {

            'Yes': True,
            'Y': True,
            '1': True,
            1: True,
            'No': False,
            '0': False,
            0: False
}


df['active'] = df['active'].map(bool_map).fillna(False).astype(bool)

print("FIX APPLIED")
print(df['active'].unique())

# ==========================================
#             DATE PARSING
# ==========================================

print(df['start_date'].dtype)

df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')
df['end_date'] = pd.to_datetime(df['end_date'], dayfirst=True, errors='coerce')

print("FIX APPLIED")
print(df['start_date'].dtype)


df = df.loc[:, ~df.columns.duplicated()]

# ==========================================
#   LOGICAL INTEGRITY (CLICKS vs IMPRESSIONS)
# ==========================================

impossible_mask = df['clicks'] > df['impressions']
print(df.loc[impossible_mask,['campaign_id','impressions','clicks']].head(3))

# ==========================================
#       LOGICAL INTEGRITY (TIME TRAVEL)
# ==========================================

time_travel_mask = df['end_date'] < df['start_date']
print(df.loc[time_travel_mask,['campaign_id','start_date','end_date']].head(3))

df.loc[time_travel_mask, 'end_date'] = df.loc[time_travel_mask, 'start_date'] + pd.Timedelta(days=30)

print("FIX APPLIED")
print(df.loc[time_travel_mask,['campaign_id','start_date','end_date']].head(3))


# ==========================================
#             HANDLING OUTLIERS 
# ==========================================

Q1 = df['spend'].quantile(0.25)
Q3 = df['spend'].quantile(0.75)

IQR = Q3 - Q1
upper_limit = Q3 + (3 * IQR)

outlier_mask = df['spend'] > upper_limit
print(df.loc[outlier_mask,['campaign_id','spend']].head(3))

print("FIX APPLIED")
df.loc[outlier_mask, 'spend'] = upper_limit
print(df.loc[outlier_mask,['campaign_id','spend']].head(3))

# ==========================================
#    STRING PARSING (FEATURE EXTRACTION)
# ==========================================

print(df['campaign_name'].head(3))

df['season'] = df['campaign_name'].str.extract(r'Q\d_([^_]+)_')

print("FIX APPLIED")

print(df[['campaign_name','season']].head(3))

# Save the cleaned data
df.to_csv('data/marketing_campaign_data_cleaned.csv', index=False)