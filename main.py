import pandas as pd


sheet_id = "19blRfJ22hYLv21SPmbmfqvRDdYy0RPX-dOLP5pN6TFw"

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

print(df.head())

# https://docs.google.com/spreadsheets/d/19blRfJ22hYLv21SPmbmfqvRDdYy0RPX-dOLP5pN6TFw/edit?usp=sharing


