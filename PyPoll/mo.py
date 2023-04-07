import os
import csv

# assiging the path of the csv file to a variable
csvpath = os.path.join('.', 'Resourcespoll', 'election_data.csv')

with open(csvpath, 'r') as csv_file:
    row_csv = csv_file.read()

with open(csvpath, 'r') as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #if data has headers 
    header_csv = next(csv_reader)
    data_csv_list = list(csv_reader)
   
#=======================================================================================================
print('Election Results')
print('------------------------')

#total number of votes can be calculated by the modual len

number_votes=len(data_csv_list)
print(f'Total Votes: {number_votes}')
print('----------------------')

#=======================================================================================================

#creating an empty dic
candidate_with_votes = {}    #  ====> {charles : 20,000 , diana : 60,000 , dave : 10,0000 }
for i in data_csv_list:
    candidate = i[2]
    if candidate in candidate_with_votes:
        candidate_with_votes[candidate] += 1
    else:
        candidate_with_votes[candidate] = 1


for candidate, votes in candidate_with_votes.items():    # dic {key: value} === > items {diana : 40000}
    vote_percentage = votes / number_votes * 100
    print(f'{candidate}: {vote_percentage:.3f}% ({votes})')

winner =''
max_votes = 0
for candidate, votes in candidate_with_votes.items(): 
    if votes > max_votes:
        max_votes = votes
        winner = candidate
print('-------------------------')       
print(f'Winner: {winner}')
# print('-------------------------')
# with open(os.path.join("outputfilepoll.txt", 'w') as file:
#     file.write('Election Results\n')
#     file.write('------------------------\n')
#     file.write(f'Total Votes: {number_votes}\n')
#     file.write('------------------------\n')
#     for candidate, votes in candidate_with_votes.items():
#         vote_percentage = votes / number_votes * 100
#         file.write(f'{candidate}: {vote_percentage:.3f}% ({votes})\n')
#     file.write('------------------------\n')
#     file.write(f'Winner: {winner}\n')
#     file.write('------------------------\n')