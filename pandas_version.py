import pandas as pd
score_csv = pd.read_csv("scores.csv")
score_csv["score"] = pd.to_numeric(score_csv["score"], errors="coerce")
score_csv["score"] = score_csv["score"].fillna(0)
result = score_csv.groupby("category")["score"].mean().round(2)
print(result)