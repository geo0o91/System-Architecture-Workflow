import pandas as pd
import numpy as np

# 1. Simulate receiving a messy, raw data feed from an external source
print("⏳ Ingesting raw external data feed...")
raw_data = {
    'Client_ID': [101, 102, np.nan, 104, 105],
    'Raw_Text': [
        "  CRITICAL: System outage reported in Learning Commons  ",
        "INFO: Routine maintenance scheduled",
        "ERROR: Database connection timeout",
        "  WARNING: High latency detected on Ottawa network  ",
        "INFO: New user onboarded successfully"
    ],
    'Priority_Score': [9.5, 2.0, 8.7, np.nan, 1.5]
}

# 2. Load the data into a Pandas DataFrame (The core tool of data engineering)
df = pd.DataFrame(raw_data)

print("\n--- RAW UNCLEANED DATA ---")
print(df)

# 3. Begin Data Engineering & Cleansing Processes
print("\n🛠️ Executing data cleaning pipeline...")

# Drop rows where the critical identifier (Client_ID) is missing
df = df.dropna(subset=['Client_ID'])

# Standardize text: Strip empty out-of-bounds spacing and convert to uppercase
df['Raw_Text'] = df['Raw_Text'].str.strip().str.upper()

# Handle missing numeric data: Replace missing Priority_Scores with a logical median value
median_priority = df['Priority_Score'].median()
df['Priority_Score'] = df['Priority_Score'].fillna(median_priority)

print("\n--- PIPELINE EXECUTION SUCCESSFUL ---")
print(df)

# 4. Export the clean data structure to a production-ready file
df.to_csv("clean_system_logs.csv", index=False)
print("\n💾 Cleaned data layer exported to 'clean_system_logs.csv' successfully.")
