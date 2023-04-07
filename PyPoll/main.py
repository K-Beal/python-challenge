import os
import csv

csvpath = os.path.join('.', 'Resourcespoll', 'election_data.csv')

#creating lists and defining variables
number_of_votes = []
list_of_candidates = []
candidates = dict()

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#the total number of votes cast    
    for row in (csvreader):
        number_of_votes.append(row[0])
# total votes per candidate
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
#percent of votes per candidate
    votes = number_of_votes[candidate]
    percent_vote = (float(votes)/float(number_of_votes) * 100)

print(f"Total Votes: {len(number_of_votes)}")
print(f"List of Candidates: {candidates}")
print(f"vote percent: {percent_vote}")