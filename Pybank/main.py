#Import the Modules we need
import os
import csv
import sys

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

    # Convert each column to lists and find sum of profits/losses
    for row in budget_csv:
        value = int(row[1])
        total += value
        dates.append(row[0])
        PnL.append(row[1])

    # Calculate the changes in profits and losses from month to month (Xpert LA)
    for i in range(len(PnL)):
        if i == 0:
            continue
        else:
            change = int(PnL[i]) - int(PnL[i-1])
            changes.append(change)

    # Calculate the average change
    average_change = sum(changes)/len(changes)

    # Find the greatest increase (best) and greatest decrease (worst) in profits
    grt_increase = max(changes)
    best_index = changes.index(grt_increase)
    best_date = dates[best_index+1] # add a row to the index because we skipped a row in 'changes'

    grt_decrease = min(changes)
    worst_index = changes.index(grt_decrease)
    worst_date = dates[worst_index+1]

# Print the Financial Analysis to terminal
    print(f'''
    Financial Analysis
          
    -------------------------------
          
    Total months: {str(len(dates))}
    
    Total: ${str(total)}

    Average Change: ${round(average_change, 2)}

    Greatest Increase in Profits: {best_date} (${grt_increase})

    Greatest Decrease in Profits: {worst_date} (${grt_decrease})
          ''')

# Create a file and print the Financial Analysis to it
file = os.path.join('analysis', 'financial_analysis.txt')

# Open/create file in write mode
with open(file, 'w') as file:
    # Redirect the standard output to text file (cr: Xpert LA)
    sys.stdout = file

    # Print to txt file
    print(f'''
    Financial Analysis
          
    -------------------------------
          
    Total months: {str(len(dates))}
    
    Total: ${str(total)}

    Average Change: ${round(average_change, 2)}

    Greatest Increase in Profits: {best_date} (${grt_increase})

    Greatest Decrease in Profits: {worst_date} (${grt_decrease})
    ''')
    
    # Restore standard output
    sys.stdout = sys.__stdout__