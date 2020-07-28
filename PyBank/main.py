import pandas as pd 

budget_df = pd.read_csv("Resources/budget_data.csv")
# total number of months
count = budget_df["Date"].value_counts()
count = count.sum()
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {count}")
# total amount of "Profit/Losses"
Total = budget_df["Profit/Losses"].sum()
print(f"Total: (${Total})")
# Average Change
Average = budget_df["Profit/Losses"].diff().mean()
print(f"Average Change: (${Average})")
#Max Increase in Profits
#diff_df = budget_df["Profit/Losses"].diff()
#diff_df.max()
#max_value = diff_df.max()
#max_val_index = diff_df.loc[diff_df["Profit/Losses"] == max_value].index[0]
#max_val_date = budget_df.iloc[max_val_index].Date
#print(f"Greatest Increase in Profits: {max_val_date} (${max_value})")


