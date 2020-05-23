#first we will import os module to allow us to create file paths accross systems
import os

#import module to read csv files
import csv

#files to load 
file_input=os.path.join("Resources","election_data.csv")

#variables to capture total votes and put the candidates in lists
total_votes=0
unique_candidates= []
candidate_vote_count= []

#open csv file
with open(file_input) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader)

#loop to capture total number of votes and per candidate. Indenting is IMPORTANT OR ELSE IT WILL NOT LOOP!!!!!!!!!!!!!
    for row in csvreader:
        total_votes +=1
        #column 3
        candidate_in=(row[2])
    #unique candidates
        if candidate_in in unique_candidates:
            candidate_index= unique_candidates.index(candidate_in)
            candidate_vote_count[candidate_index]=candidate_vote_count[candidate_index]+1
        else:
            unique_candidates.append(candidate_in)
            candidate_vote_count.append(1)
# variables for candidate list
candidate_list=[]
max_votes= candidate_vote_count[0]
max_index=0

#loop to find who the winner is
for i in range(len(unique_candidates)):
    votes_per_c=round(candidate_vote_count[i]/total_votes*100,2)
    candidate_list.append(votes_per_c)

    if candidate_vote_count [i] > max_votes:
        max_votes= candidate_vote_count[i]
        max_index= i

winner=unique_candidates[max_index]

#gitbash
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
#instead of hardcoding each candidate, you can use a loop to display candidate numbers
for i in range(len(unique_candidates)):
    print(f'{unique_candidates[i]} : {candidate_list[i]}% ({candidate_vote_count[i]})')
print("-------------------------")
print("Election Winner: "+ str(winner))
print("-------------------------")

#export to text file
file_output=os.path.join("analysis","budget_analysis.txt")
#using the f function in this script
with open(file_output,"w", newline="") as exportfile:
    exportfile.write("-------------------------\n")
    exportfile.write("     Election Results     \n")
    exportfile.write("-------------------------\n")
    exportfile.write(f'Total Votes: {total_votes}\n')
    exportfile.write("-------------------------\n")
    for i in range(len(unique_candidates)):
        exportfile.write(f'{unique_candidates[i]} : {candidate_list[i]}% ({candidate_vote_count[i]})')
    exportfile.write("-------------------------\n")
    exportfile.write(f'Election winner: {winner}\n')