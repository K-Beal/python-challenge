import os
import csv

csvpath = os.path.join('.', 'Resourcespoll', 'election_data.csv')

#creating lists
number_of_votes = []
list_of_candidates = []
#defining variable
candidate = row[2]
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#the total number of votes cast    
    for row in (csvreader):
        number_of_votes.append(row[0])
        list_of_candidates.append(row[2])
        # candidate = str(row[2])
        if candidate in list_of_candidates:
            list_of_candidates[candidate] += 1
        else:
            list_of_candidates[candidate] = 1

print(f"Total Votes: {len(number_of_votes)}")
print(f"List of Candidates: {list_of_candidates}")


# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# some_dict = {
#     "Charles Casper Stockham": 17,
#     "Diana DeGette": 39,
#     "Raymon Anthony Doane": 40
# }

# for key in some_dict.keys():
#     print(key) # John, Savannah, Steve
    
# for value in some_dict.values():
#     print(value) # 17, 39, 40

# for key, value in some_dict.items():
#     print(key, value) # John 17, Savannah 39, Steve 40

# name = "John"    
# if name in some_dict:
#     print(f"{name} is in some_dict and has {some_dict['John']} votes.")

# if name in some_dict:
#     # This is not the first time someone has voted for name...
#     # Increment their vote count by 1...
#     some_dict[name] = some_dict[name] + 1
# else:
#     # This is the first time soeone has voted for name...
#     # Add name to dict and set initial vote count to 1...
#     some_dict[name] = 1