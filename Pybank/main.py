#Import the Modules we need
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Put the data from "columns" into lists
dates = []
PnL = []
changes = [] # create new list to store the changes in profits/losses by month

# Test our list success
with open(csvpath) as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')

    csv_header = next(budget_csv)

    # add each column to lists by row
    for row in budget_csv:
        dates.append(row[0])
        PnL.append(row[1])

    for i in range(len(PnL)):
        if i == 0:
            changes.append(int(PnL[i]))
        else:
            change = int(PnL[i]) - int(PnL[i-1])
            changes.append(change)
    print(len(changes))
    #Calculate the average change - working on this
    #average = sum(changes)/len(changes)
    
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total months: " + str(len(dates)))