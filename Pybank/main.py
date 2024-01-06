#Import the Modules we need
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Put the data from "columns" into lists and declare any variables will need to use

dates = []
PnL = []
changes = [] # create new list to store the changes in profits/losses by month
total = 0

# Open the CSV file for PyBank calculations

with open(csvpath) as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')

    # Skip the header row and store it in a list
    csv_header = next(budget_csv)
    headers_list = list(csv_header)

    # Convert each column to lists and find sum of profits/losses
    for row in budget_csv:
        value = int(row[1])
        total += value
        dates.append(row[0])
        PnL.append(row[1])

    for i in range(len(PnL)):
        if i == 0:
            continue
        else:
            change = int(PnL[i]) - int(PnL[i-1])
            changes.append(change)

    # Calculate the average change
    average_change = sum(changes)/len(changes)

    # Print the Financial Analysis
    print(csv_header)
    print(f"""
    Financial Analysis
          
    -------------------------------
          
    Total months: {str(len(dates))}
    
    Total: ${str(total)}

    Average Change: ${round(average_change, 2)}

    Greatest Increase in Profits: ()

    Greatest Decrease in Profits: ()
          """)