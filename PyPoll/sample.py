import os
import csv

csvpath = os.path.join('.', 'Resourcespoll', 'election_data.csv')

#defining variables
total_votes = 0
candidate_index = []
number_votes = dict()

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #calculate total number of votes
    for row in csvreader:
        total_votes += 1

        candidate_1 = row[2]
        if candidate_1 not in candidate_index:
                candidate_index.append(candidate_1)
                number_votes[candidate_1] = 0
        number_votes[candidate_1] += 1

    print("Total Votes:", total_votes)

    #calculating candidate vote and percentage
    for candidate_1 in number_votes:
        votes = number_votes[candidate_1]
        vote_percentage = round ((100 * float(votes)/float(total_votes)),3)

        candidate_result = (f"{candidate_1}: {vote_percentage}% ({votes:})")
        print(candidate_result)

        winner = (max(number_votes, key=number_votes.get))