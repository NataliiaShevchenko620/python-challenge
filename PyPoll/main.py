import os
import csv

#despite of the fact that this function is executed only once, 
#I decided to move the main logic of the task into the function, because functions were in scope of this module
def election_results(election_data_csv):
    #define lists for main calculations
    total_votes = 0
    winner_votes = 0
    candidate_votes = {}
    election_results = []

    #reading from a source CSV file
    with open(election_data_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        next(csvreader, None)  #skip the headers

        #reading each row in the CSV file and retrieving info about each vote
        for row in csvreader:
            #calculate total votes
            total_votes = total_votes + 1

            #get candidate name
            candidate = row[2]
            
            #count the votes for each candidate and store the result in a dictionary
            #if no such candidate in a dictionary yet, then add it, otherwise, update the number of votes
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
        
    #find the winner of the election based on popular vote
    for candidate, votes in candidate_votes.items():
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate

    #generate election results as a list
    #using list here as an alternative to tuple way to store the result
    election_results.append("Election Results")
    election_results.append("----------------------------")
    election_results.append(f"Total Votes: {total_votes}")
    election_results.append("----------------------------")
    #iterate over a dictionary to calculate percentage of votes for each candidate
    for candidate, votes in candidate_votes.items():
        election_results.append(f"{candidate}: {100* votes / total_votes:.3f}% ({votes})")
    election_results.append("-------------------------")
    election_results.append(f"Winner: {winner}")
    election_results.append("-------------------------")

    #print the analysis to the terminal
    for s in election_results:
        print(s)

    #export a text file with the results
    election_results_txt_path = os.path.join(".", "analysis", "election_results.txt")
    with open(election_results_txt_path, "w") as datafile:
        for l in election_results:
            datafile.write(l + "\n")

#set a path to a source file to pass it to the function
election_data_csv = os.path.join(".", "Resources", "election_data.csv")

#execute the function that performs the main logic of the task
election_results(election_data_csv)
