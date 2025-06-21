
import pandas as pd

def calculate_nti(fts_z, prs_z, alpha=0.5):
    return alpha * fts_z + (1 - alpha) * prs_z

# Example usage:
# df = pd.read_csv("data/FTS_by_population.csv")
# df["NTI"] = calculate_nti(df["FTS (z-score)"], df["PRS (z-score)"])
