import os
import csv

# reading csv file
election_data = os.path.join("Resources","election_data.csv")

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    # calculating total votes
    vote_list=[row[2] for row in csvreader] 
    total_votes = len(vote_list)

# creating candidate list 
cand_list = [] 
for x in vote_list:
    if x not in cand_list:
        cand_list.append(x)

# calculating each candidate votes and percentage
cand_num_list = [] 
cand_percent_list = []
cand_num_list = [vote_list.count(item) for item in cand_list] 
z = 0
while z < len(cand_num_list):
    cand_percent_list.append(cand_num_list[z]/total_votes)
    z = z + 1
 
# The Winner
win_index = 0
win_index = cand_num_list.index(max(cand_num_list))
win = cand_list[win_index]

# print to terminal
print("\nElection Results")
print("------------------------------")
print(f"Total Votes:  {total_votes}")
print("------------------------------")
print(cand_list[0] + ': ' + "{:.3%}".format(cand_percent_list[0]) + ' ' + '(' + str(cand_num_list[0]) + ')')
print(cand_list[1] + ': ' + "{:.3%}".format(cand_percent_list[1]) + ' ' + '(' + str(cand_num_list[1]) + ')')
print(cand_list[2] + ': ' + "{:.3%}".format(cand_percent_list[2]) + ' ' + '(' + str(cand_num_list[2]) + ')')
print(cand_list[3] + ': ' + "{:.3%}".format(cand_percent_list[3]) + ' ' + '(' + str(cand_num_list[3]) + ')')
print("------------------------------")
print(f"Winner: {win}")
print("------------------------------")

# write to txt file
file_to_output = os.path.join("Analysis", "election_analysis.txt")
a = "\nElection Results"
b = "------------------------------"
c = f"Total Votes:  {total_votes}"
d = "------------------------------"
e = cand_list[0] + ': ' + "{:.3%}".format(cand_percent_list[0]) + ' ' + '(' + str(cand_num_list[0]) + ')'
f = cand_list[1] + ': ' + "{:.3%}".format(cand_percent_list[1]) + ' ' + '(' + str(cand_num_list[1]) + ')'
g = cand_list[2] + ': ' + "{:.3%}".format(cand_percent_list[2]) + ' ' + '(' + str(cand_num_list[2]) + ')'
h = cand_list[3] + ': ' + "{:.3%}".format(cand_percent_list[3]) + ' ' + '(' + str(cand_num_list[3]) + ')'
i = "------------------------------"
j = f"Winner: {win}"
k = "------------------------------"
n = '\n' 

output = f'{a} \n{b} \n{c} \n{d} \n{e} \n{f} \n{g} \n{h} \n{i} \n{j} \n{k}'
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

    