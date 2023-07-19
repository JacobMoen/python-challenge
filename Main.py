# Add dependencies
import os
import csv

# creating a file path for the csv
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# exporting the results to a csv
outputpath = os.path.join("PyBank", "Analysis", "Budget_Analysis.txt")

# assigning variables
totalmonths = 0
totalnet = 0
changelist = []
monthofchangelist = []
maxincrease = ["", 0]
maxdecrease = ["", 9999999999]

# open and read the csv file
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    # variables for For loop
    header = next(reader)
    firstrow = next(reader)
    totalmonths = totalmonths + 1
    totalnet = totalnet + int(firstrow[1])
    prevnet = int(firstrow[1])

    for row in reader:
        totalmonths = totalmonths + 1
        totalnet = totalnet + int(row[1])
        netchange = int(row[1]) - prevnet
        prevnet = int(row[1])
        changelist.append(netchange)
        monthofchangelist.append(row[0])

        if netchange > maxincrease[1]:
            maxincrease[1] = netchange
            maxincrease[0] = row[0]
        if netchange < maxdecrease[1]:
            maxdecrease[1] = netchange
            maxdecrease[0] = row[0]  

monthly_avg = sum(changelist)/len(changelist)

# output results
output = f"""
Financial Analysis
----------------------------
Total Months: {totalmonths}
Total: ${totalnet}
Average Change: ${monthly_avg:.2f}
Greatest Increase in Profits: {maxincrease[0]} (${maxincrease[1]})
Greatest Decrease in Profits: {maxdecrease[0]} (${maxdecrease[1]})
"""
print(output)

with open(outputpath, "w") as file:
    file.write(output)