import csv 
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read in CSV file
csv_data_path = os.path.join("Resources", "election_data.csv")
print(csv_data_path)

#Assigns variables to indexes
BALLOT_ID_INDEX = 0
COUNTY_INDEX = 1
CANDIDATE_INDEX = 2
#reads in a csv file
with open(csv_data_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)

    #initializing variables
    ballot_count = 0
    candidate_dict = {}
    percentage_dict = {}
    highest_vote_count = 0
    winner = None

    for row in csvreader:
        #Performs count of total number of ballots
        ballot_count = ballot_count + 1

        candidate_name = row[CANDIDATE_INDEX]
        #For every candidate in dictionary, we will count the number of votes they received.  
        if candidate_name in candidate_dict:
            vote_count = candidate_dict[candidate_name] + 1
            candidate_dict[candidate_name] = vote_count
        else:
            #If candidate doesnt exist in dictionary, we will add them to the dictionary
            candidate_dict[candidate_name] = 1
    for c in candidate_dict.items():
        vote_count = c[1]
        candidate_name = c[0]
        #Calculates running max of the vote count for each candidate and will identify the person with highest vote count 
        # as the winner
        if (vote_count > highest_vote_count):
            winner = candidate_name
            highest_vote_count = vote_count
        #Calculate the percentage vote count for each candidate  
        percentage = vote_count/ballot_count
        percentage_dict[candidate_name] = round(percentage * 100, 3)

#Prints results
print('Election Results')
print('-------------------------')
print(f"Total Votes: {ballot_count}")
print('-------------------------')
for c in candidate_dict.items():
    print(f"{c[0]}: {percentage_dict[c[0]]}% ({c[1]})")
print('-------------------------')
print(f"Winner: {winner}")
print('-------------------------')
#Exports to text file
with open('Analysis/pypoll.txt', 'a') as pp:
    pp.write('Election Results' + "\n")
    pp.write('-------------------------' + "\n")
    pp.write(f"Total Votes: {ballot_count}" + "\n")
    pp.write('-------------------------' + "\n")
    for c in candidate_dict.items():
        pp.write(f"{c[0]}: {percentage_dict[c[0]]}% ({c[1]})" + "\n")
    pp.write('-------------------------' + "\n")
    pp.write(f"Winner: {winner}" + "\n")
    pp.write('-------------------------')

    
    

