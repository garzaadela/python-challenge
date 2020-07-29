import pandas as pd 

pypoll_df = pd.read_csv("Resources/election_data.csv")

# Total number of votes
count = pypoll_df["Voter ID"].value_counts()
total_votes = count.sum()
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")

# complete list of candidates 
list_candidates = list(pypoll_df["Candidate"].unique())


# The winner based on popular vote

# The total number of votes each candidate won
candidate_votes = pypoll_df.groupby("Candidate")["Voter ID"].count()
candidate_votes = candidate_votes.to_frame()
candidate_votes.reset_index(inplace = True)

# The percentage of votes each candidate won
candidate_votes["Percentage"] = candidate_votes["Voter ID"]/total_votes
for i,row in candidate_votes.iterrows():
    name = row["Candidate"]
    percentage = row["Percentage"]
    votes = row["Voter ID"]
    print(f"{name}: {percentage :.3%} ({votes})")
       

print("------------------------")

# Winner of the election
winner = candidate_votes["Voter ID"].max()
Winner_name = candidate_votes.loc[candidate_votes["Voter ID"] == winner]["Candidate"].values
Winner_name = Winner_name[0]
print(f"Winner: {Winner_name}")
print("---------------------------")