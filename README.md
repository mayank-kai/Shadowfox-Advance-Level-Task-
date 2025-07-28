# Shadowfox-Advance-Level-Task-
Cricket Fielding Analysis
# 🏏 Fielding Performance Evaluation - IPL Case Study

This project is a Python-based data analytics solution to evaluate fielding performance in an IPL cricket match. Using custom-defined fielding metrics and a weighted scoring system, it ranks players based on their performance.

---

## 📌 Objective

To assess and rank players in a cricket match based on their fielding contributions such as clean picks, catches, throws, direct hits, and runs saved using a structured scoring methodology.

---

## 📁 Dataset Overview

The dataset includes ball-by-ball fielding events from a single match:

| Column Name     | Description                             |
|------------------|------------------------------------------|
| Match No.        | Unique match identifier                  |
| Innings          | Innings number (1 or 2)                  |
| Team             | Team name (e.g., Delhi Capitals)         |
| Player Name      | Fielding player name                     |
| BallCount        | Ball number (e.g., 1.1, 0.5)             |
| Position         | Fielding position                        |
| Pick             | Fielding action (Y, C, DC, DH)           |
| Throw            | Throw outcome (Y, RO, MR, S)             |
| Runs             | Runs saved or conceded by fielder        |

---

## 🧮 Metrics Calculated

The following key fielding indicators are tracked:

- ✅ Clean Picks (CP)
- 🎯 Good Throws (GT)
- 👐 Catches (C)
- ❌ Dropped Catches (DC)
- 🔁 Stumpings (S)
- 🔥 Run Outs (RO)
- 😞 Missed Run Outs (MR)
- 🎯 Direct Hits (DH)
- 💰 Runs Saved (RS)

---

## ⚖️ Weighted Scoring System

Each metric contributes to a player's **Performance Score (PS)** based on the following weightings:

| Metric            | Weight |
|--------------------|--------|
| Clean Pick (CP)    | +1     |
| Good Throw (GT)    | +1     |
| Catch (C)          | +3     |
| Dropped Catch (DC) | -3     |
| Stumping (S)       | +3     |
| Run Out (RO)       | +3     |
| Missed Run Out (MR)| -2     |
| Direct Hit (DH)    | +2     |
| Runs Saved (RS)    | +1     |

---

## 📊 Output

A sorted performance matrix is generated as a `pandas` DataFrame showing player stats and total scores.

Sample output:

📊 Fielding Performance Matrix:
  Player Name  Clean Picks (CP)  Good Throws (GT)  Catches (C)  Dropped Catches (DC)  Stumpings (S)  Run Outs (RO)  Missed Run Outs (MR)  Direct Hits (DH)  Runs Saved (RS)  Performance Score (PS)
Kuldeep yadav                 3                 0            0                     0              0              0                     0                 0                4                       7
   Yash Dhull                 1                 1            0                     0              0              0                     0                 0                3                       5
    Aman Khan                 2                 1            0                     0              0              0                     0                 0                1                       4
  Lalit yadav                 3                 2            0                     0              0              0                     0                 0               -2                       3
Rilee russouw                 0                 1            0                     0              0              0                     0                 0                1                       2
   Axer Patel                 1                 1            0                     0              0              0                     0                 0                0                       2
    Phil Salt                 1                 1            0                     0              0              0                     0                 0               -1                       1

