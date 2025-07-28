import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fielding_dataset.csv")

data = [
    ["IPL2367", 1, "Delhi Capitals", "Rilee russouw", 0.1, "Short mid wicket", "n", "Y", 1],
    ["IPL2367", 1, "Delhi Capitals", "Phil Salt", 0.2, "Wicket keeper", "Y", "Y", -1],
    ["IPL2367", 1, "Delhi Capitals", "Yash Dhull", 0.3, "Covers", "Y", "Y", 3],
    ["IPL2367", 1, "Delhi Capitals", "Axer Patel", 0.4, "Point", "Y", "Y", 0],
    ["IPL2367", 1, "Delhi Capitals", "Lalit yadav", 0.5, "Cover point", "Y", "Y", -2],
    ["IPL2367", 1, "Delhi Capitals", "Lalit yadav", 0.6, "Long off", "Y", "", 0],
    ["IPL2367", 1, "Delhi Capitals", "Aman Khan", 1.1, "Short mid wicket", "Y", "Y", 1],
    ["IPL2367", 1, "Delhi Capitals", "Aman Khan", 1.2, "Point", "Y", "", 0],
    ["IPL2367", 1, "Delhi Capitals", "Kuldeep yadav", 1.3, "Short mid wicket", "Y", "", 4],
    ["IPL2367", 1, "Delhi Capitals", "Kuldeep yadav", 1.4, "Point", "Y", "", 0],
    ["IPL2367", 1, "Delhi Capitals", "Kuldeep yadav", 1.5, "Bowler", "Y", "", 0],
    ["IPL2367", 1, "Delhi Capitals", "Lalit yadav", 1.6, "Bowler", "Y", "Y", 0],
]

columns = [
    "Match No.", "Innings", "Team", "Player Name", "BallCount", "Position",
    "Pick", "Throw", "Runs"
]

df = pd.DataFrame(data, columns=columns)

# Initialize metrics
players = df["Player Name"].unique()

# Create empty stats dict
stats = {player: {
    "Clean Picks (CP)": 0,
    "Good Throws (GT)": 0,
    "Catches (C)": 0,
    "Dropped Catches (DC)": 0,
    "Stumpings (S)": 0,
    "Run Outs (RO)": 0,
    "Missed Run Outs (MR)": 0,
    "Direct Hits (DH)": 0,
    "Runs Saved (RS)": 0,
} for player in players}

# Mapping values from screenshot rules
for _, row in df.iterrows():
    p = row["Player Name"]
    pick = row["Pick"]
    throw = row["Throw"]
    runs = row["Runs"]

    if pick == "Y":
        stats[p]["Clean Picks (CP)"] += 1
    if pick == "C":
        stats[p]["Catches (C)"] += 1
    if pick == "DC":
        stats[p]["Dropped Catches (DC)"] += 1
    if pick == "DH":
        stats[p]["Direct Hits (DH)"] += 1

    if throw == "Y":
        stats[p]["Good Throws (GT)"] += 1
    if throw == "RO":
        stats[p]["Run Outs (RO)"] += 1
    if throw == "S":
        stats[p]["Stumpings (S)"] += 1
    if throw == "MR":
        stats[p]["Missed Run Outs (MR)"] += 1

    stats[p]["Runs Saved (RS)"] += runs

# Weights
weights = {
    "Clean Picks (CP)": 1,
    "Good Throws (GT)": 1,
    "Catches (C)": 3,
    "Dropped Catches (DC)": -3,
    "Stumpings (S)": 3,
    "Run Outs (RO)": 3,
    "Missed Run Outs (MR)": -2,
    "Direct Hits (DH)": 2,
    "Runs Saved (RS)": 1  # direct add
}

# Compute performance score
for p in stats:
    score = sum(stats[p][k] * weights.get(k, 1) for k in stats[p])
    stats[p]["Performance Score (PS)"] = score

# Convert to DataFrame
result_df = pd.DataFrame.from_dict(stats, orient="index").reset_index()
result_df = result_df.rename(columns={"index": "Player Name"})

# Reorder for clarity
cols = [
    "Player Name", "Clean Picks (CP)", "Good Throws (GT)", "Catches (C)", "Dropped Catches (DC)",
    "Stumpings (S)", "Run Outs (RO)", "Missed Run Outs (MR)", "Direct Hits (DH)", "Runs Saved (RS)",
    "Performance Score (PS)"
]
result_df = result_df[cols]

# Display Matrix
print("\n📊 Fielding Performance Matrix:")
print(result_df.sort_values(by="Performance Score (PS)", ascending=False).to_string(index=False))