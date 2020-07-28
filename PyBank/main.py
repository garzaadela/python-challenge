import pandas as pd 

budget_df = pd.read_csv("Resources/budget_data.csv")
# total number of months
count = budget_df["Date"].value_counts()
count = count.sum()
print("Financial Analysis")
print("-----------------------------")
print(f"Total: {count}")