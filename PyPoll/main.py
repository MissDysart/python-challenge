#Import the Modules we need
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Put the data from "columns" into lists and declare any variables will use
ballots = []
counties = []
candidates = []

# Open the CSV file for PyPoll

with open(csvpath) as csvfile:
    election_csv = csv.reader(csvfile, delimiter=',')

    # Skip the header row and store it in a list
    election_header = next(election_csv)

    for vote in election_csv:    
        ballots.append(vote[0])
        counties.append(vote[1])
        candidates.append(vote[2])

    


# Show Election Results in terminal
    print(f"""
        Election Results
          
        -------------------------------
        
        Total votes: {str(len(ballots))}

        -------------------------------
        """)