
import os
import csv

#Imports election_data_1.csv

election_data_1=os.path.join('python-challenge','election_data_1.csv')


with open(election_data_1, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    for row in csvreader:
        print(row)
    

#Imports election_data_2.csv

election_data_2=os.path.join('python-challenge','election_data_2.csv')

with open(election_data_2, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    for row in csvreader:
        print(row)
    

###########
#Create lists for appended data
Total_Votes=[]
Candidate_List=[]
Percentage_Votes=[]
Candidate_Votes=[]
Winner=[]

############
Total_Votes=len(Candidate_Votes)
Total_Votes=int(Total_Votes)

count = 0
#list of candidates (unique names) who received votes
Candidate_List = set(Candidate_Votes)
Candidates=[]

###########

#Create Election Results table

print("Election Results")
print("------------------------")
print("Total Votes: ", Total_Votes)
print("------------------------")

for row in Candidate_List:
    Candidates.append(row)
    Candidate Name=str(Candidates[count])
    percentage= Candidate_Votes/Total_Votes*100
    print(Candidates, Percentage, Number of Votes )
    count=count+1
    
