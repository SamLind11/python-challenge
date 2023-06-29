# Import statements.
import os
import csv

# Create file path for reading budget_data.csv file.
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Convert data to nested list.
    dataList = list(csvreader)

    # Remove header row.
    dataList.remove(dataList[0])

    # Tracking variables
    numMonths = len(dataList)
    netTotal = 0
    totalChanges = 0
    greatestIncrease = 0
    greatestIncreaseDate = ""
    greatestDecrease = 0
    greatestDecreaseDate = ""

    # Iterate through dataList.
    for i in range(numMonths):

        # Add Profit/Losses value to running total
        netTotal += int(dataList[i][1])

        if(i != (numMonths - 1)):
            thisChange = int(dataList[i + 1][1]) - int(dataList[i][1])
            totalChanges += thisChange

            if (thisChange > greatestIncrease):
                greatestIncrease = thisChange
                greatestIncreaseDate = dataList[i + 1][0]
            
            if (thisChange < greatestDecrease):
                greatestDecrease = thisChange
                greatestDecreaseDate = dataList[i + 1][0]

    # Print data analysis in terminal.
    print("Financial Analysis")
    print("-"*25)

    print(f"Total Months: {numMonths}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${round(totalChanges/(numMonths - 1),2)}")
    print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})")

    # Writes results to a file called bankAnalysis.txt.
    bankPath = os.path.join('analysis', 'bankAnalysis.txt')

    with open(bankPath, "w") as file:
        file.write("Financial Analysis\n")
        file.write("-"*25 + "\n")
        file.write(f"Total Months: {numMonths}\n")
        file.write(f"Total: ${netTotal}\n")
        file.write(f"Average Change: ${round(totalChanges/(numMonths - 1),2)}\n")
        file.write(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})\n")
        file.write(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})\n")
    
        file.close()

    