#Import the Modules needed
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Put the data from "columns" into lists and declare any variables will use
ballots = []
counties = []
choice = []
vote_count = {}

# Open the CSV file for PyPoll

with open(csvpath) as csvfile:
    election_csv = csv.reader(csvfile, delimiter=',')

    # Skip the header row and store it in a list
    election_header = next(election_csv)

    # Add ballots, counties, and choice to lists
    for row in election_csv:
        ballots.append(row[0])
        counties.append(row[1])
        choice.append(row[2])

    # Find the total number of votes
    total_votes = len(ballots)

    # Find the candidates and number of votes they each received (code from Xpert LA)
    for candidate in choice:
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1
   
    # Find the winner based on popular vote
    most_votes = max(vote_count.values())
    winner = max(vote_count, key=vote_count.get)

# Show Election Results in terminal/text file
#with open('results.txt', 'w') as txt_file:
#txt_file.write(Election Results)
print(f"""
Election Results
      
-------------------------------
      
Total votes: {total_votes}

-------------------------------
""")
# Find the percentage of votes each candidate received and print
for candidate, count in vote_count.items():
    percentage = round(count/total_votes * 100, 3)
    print(f'{candidate}: {percentage}% ({count})\n')
print(f"""
--------------------------------
      
Winner: {winner}

--------------------------------
""")