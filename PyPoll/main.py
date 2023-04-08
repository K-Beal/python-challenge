import os
import csv

csvpath = os.path.join('.', 'Resourcespoll', 'election_data.csv')

#creating lists and defining variables

candidates = dict()
total_votes = 0
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #the total number of votes cast    
    for row in (csvreader):
        total_votes += 1
        # total votes per candidate
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Find the Winner
winner = ""
most_votes = max(candidates.values())
for candidate in candidates:
    if candidates[candidate] == most_votes:
        winner = candidate
print(f"Total Votes: {total_votes}")
#Find percent of votes won per candidate
for candidate in candidates:
    percent_vote = 100 * candidates[candidate] / total_votes
    # print(candidate, percent_vote)
    print(f"Vote Percentage: {candidate}, {percent_vote:0.3f}, ({candidates[candidate]})")
# num_vote = total_votes/percent_vote
# print(num_vote)
print(f"Winner: {winner}")

with open(os.path.join("output-file.txt"), "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("---------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("---------------------\n")
    for candidate in candidates:
        percent_vote = 100 * candidates[candidate] / total_votes
        textfile.write(f"Vote Percentage: {candidate}, {percent_vote:0.3f}%, ({candidates[candidate]})\n")
    textfile.write("---------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("---------------------\n")