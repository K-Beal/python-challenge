import os
import csv

csvpath = os.path.join('.','Resources', 'budget_data.csv')
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row[1])
# total number of months "Profit/Losses" over the entire period
    
# net total amount of "Profit/Losses" over the entire period
        total = 0
        total = sum(["Profit/Losses"])
        print(total)
# changes in profit/losses over entire period

# average of those changes

# greatest increase in profits (date and amount) over entire period

# greatest decrease in profits (date and amount) over entire period