# Add dependencies
# inspiration from eddiexunyc
import os
import csv

# assigning variables
candidates = {}
break_line = "------------------------------"

# creating a file path for the csv
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# output results to text file
output_result = os.path.join("PyPoll", "analysis", "election_results.txt")

# open and read the csv file to get candidates
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    header = next(reader)
    total_vote = 0
    for row in reader:
        total_vote = total_vote + 1
        name = row[2]
        if name in candidates:
            candidates[name] = candidates[name] + 1
        else:
            candidates[name] = 1
    
candidates["Charles Percent"] = round((candidates["Charles"]/total_vote) * 100, 2)
candidates["Diana Percent"] = round((candidates["Diana"]/total_vote) * 100, 2)
candidates["Raymon Percent"] = round((candidates["Raymon"]/total_vote) * 100, 2)

# calculate the winner
cand_winner = max(candidates, key=candidates.get)

# print out results
print("Election Results")
print(break_line)
print("Total Vote: " + str(total_vote))
print(break_line)
print("Charles: " + str(candidates["Charles Percent"]) + "% " + str(candidates["Charles"])) 
print("Diana: " + str(candidates["Diana Percent"]) + "% " + str(candidates["Diana"]))
print("Raymon: " + str(candidates["Raymon Percent"]) + "% " + str(candidates["Raymon"]))
print(break_line)
print("Winner: " + str(cand_winner))
print(break_line)

# open and read the csv file
with open(output_result, "w") as txt_file:
    txt_file.write("Election Results" + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Total Vote: " + str(total_vote) + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Charles: " + str(candidates["Charles Percent"]) + "% " + str(candidates["Charles"]) + "\n") 
    txt_file.write("Diana: " + str(candidates["Diana Percent"]) + "% " + str(candidates["Diana"]) + "\n")
    txt_file.write("Raymon: " + str(candidates["Raymon Percent"]) + "% " + str(candidates["Raymon"]) + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Winner: " + str(cand_winner) + "\n")
    txt_file.write(break_line + "\n")
