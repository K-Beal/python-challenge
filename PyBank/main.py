import os
import csv

csvpath = os.path.join('.','Resources', 'budget_data.csv')
months = []
change_list = []
change_months = []
total = 0
prior = 0
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for index,row in enumerate(csvreader):
        if row[0] not in months:
            months.append(row[0])
        total = total + int(row[1])
        if index == 0:
            prior = int(row[1])
        else:
            change = int(row[1]) - prior
            prior = int(row[1])
            change_list.append(change)
            change_months.append(row[0])
mean_change = sum(change_list)/len(change_list)

max_index = change_list.index(max(change_list))
min_index = change_list.index(min(change_list))       
print(f"Total Months: {len(months)}")
# changes in profit/losses over entire period
print(f"Total: ${total}")

# average of those changes
print(f"Average Change: ${mean_change:0.2f}")

# greatest decrease in profits (date and amount) over entire period
print(f"Greatest Increase in Profits: {change_months[max_index]} (${change_list[max_index]})")

# greatest increase in profits (date and amount) over entire period
print(f"Greatest Decrease in Profits: {change_months[min_index]} (${change_list[min_index]})")

with open(os.path.join("output-file.txt"), "w") as textfile:
    textfile.write(main.py)