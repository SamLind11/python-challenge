#Import Statements
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Convert data to nested list.
    dataList = list(csvreader)

    #Remove header row.
    dataList.remove(dataList[0])

    #Number of votes.
    numVotes = len(dataList)

    #Lists to hold election candidates results.
    candidates = []
    candidateVotes = []
    electionWinnerVotes = 0

    #Loop which iterates through each row of the csv file.
    for i in range(numVotes):
        if (candidates.count(dataList[i][2]) == 0):
            candidates.append(dataList[i][2])
            candidateVotes.append(1)
        else:
            candidateVotes[candidates.index(dataList[i][2])] += 1
    



    print("Election Results")
    print("-"*25)
    print(f"Total votes: {numVotes}")
    print("-"*25)


    #Prints election results.
    for i in range(len(candidates)):

        #Calculates the percent of total votes won by the candidate.
        percentOfVote = round((candidateVotes[i]/numVotes) * 100, 3)

        #Checks for highest vote count
        if (candidateVotes[i] > electionWinnerVotes):
            electionWinnerVotes = candidateVotes[i]

        print(f"{candidates[i]}: {percentOfVote}% ({candidateVotes[i]})")

    print("-"*25)
    print(f"Winner: {candidates[candidateVotes.index(electionWinnerVotes)]}")

    #Code for writing results to text file called electionResults.txt
    electionResultsPath = os.path.join('analysis','electionResults.txt')

    with open(electionResultsPath, "w") as file:
        file.write("Election Results\n")
        file.write("-"*25 + "\n")
        file.write(f"Total Votes: {numVotes}\n")
        file.write("-"*25 + "\n")

        for i in range(len(candidates)):
            percentOfVote = round((candidateVotes[i]/numVotes) * 100, 3)

            file.write(f"{candidates[i]}: {percentOfVote}% ({candidateVotes[i]})\n")
        file.write("-"*25 + "\n")
        file.write(f"Winner: {candidates[candidateVotes.index(electionWinnerVotes)]}\n")
        file.write("-"*25 + "\n")

    file.close

