#THIS CODE HAS BEEN DERIVED FROM BUT NOT LIMITED TO YOUTUBE, WWW3SCHOOL, ZOOM CLASS RECORDING ETC 


#IMPORT MODULE OS 
import os

# MODULE FOR READING CSV FILES
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")

#DECLAREING ALL VARIABLES 
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0
#OPEN FILE PATH FOR READING ONLY  ELECTION_DATA.CSV
with open(csvpath, "r") as file:
    reader = csv.reader(file)

    # SKIP FIRST OR (HEADER ROW)
    next(reader)
    #FOR LOOP THROUGH THE ROWS 
    for row in reader:
        # GET VOTER ID , COUTY CANDIDATE 
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        # TOTAL VOTE TO BE INCREMENT
        total_votes += 1
        
        #VOTERS BEING ADDED TO DICTIONARY OR ICREMENT THEIR VOTE COUNT 
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

#PRINT ELECTION RESULT IN CURRENT TERMINAL 
print("Election Results")
print("-" * 50)
print(f"Total Votes: {total_votes}")
print("-" * 50)

# FOR LOOP WITHIN THE CANDIDATES DICTIONARY 
for candidate, votes in candidates.items():
    
    #CALCULATE PERCENTAGE OF VOTING 
    percentage = votes / total_votes * 100
    
    #PRINT CANDIANTED NAME , PERCENTAGE , VOTES
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # IF STATEMENT VALIDATED COMPARES THE VOTES AGAINST THE CURRENT WINNER 
    if votes > winner_votes:
        # UPDATE WINNER AND VOTES
        winner = candidate
        winner_votes = votes
# DECLARE THE WINNER 
print("-" * 50)
print(f"Winner: {winner}")
print("-" * 50)


#EXPORT THE CURRENT RESULTS TO FILE NAME ELECTION_RESULTS.TXT
output_path = "election_results.txt"
with open(output_path, "w") as file:
    file.write("Election Results\n")
    file.write("-" * 50 + "\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-" * 50 + "\n")
    for candidate, votes in candidates.items():
        percentage = votes / total_votes * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-" * 50 + "\n")
    file.write(f"Winner: {winner}\n")
    file.write("-" * 50 + "\n")

