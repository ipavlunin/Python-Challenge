import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")

# reading csv file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    month_num = 0
    net_total = 0
    this_dict = {}
    
    # combining row lists into one dictionary
    for row in csvreader:
        if row[0] != 0:
            month_num +=1
            this_dict[row[0]] = row[1]

# converting dictionary values to list    
this_dict_list = list(this_dict.values())

# converting dictionary keys to list
diff_keys = list(this_dict.keys())

# removing first month from the list
diff_keys.pop(0)

# converting list items to integers                   
this_dict_list = [int(i) for i in this_dict_list]

# calculating sum of items in the list
net_total = sum(this_dict_list)

# creating a new list and populating calculated difference between months
diff = []
diff = [this_dict_list[i+1] - this_dict_list[i] for i in range(len(this_dict_list)-1)]

# calculating difference numbers average
avg = sum(diff) / (month_num - 1)

# finding greatest increase and decrease
month_indx_maxim = diff.index(max(diff))
maxim_month = diff_keys[month_indx_maxim]
month_indx_minim = diff.index(min(diff))
minim_month = diff_keys[month_indx_minim]
maxim = max(diff)
minim = min(diff)

# printing to terminal
print("\nFinancial Analysis")
print("---------------------------------------------------")
print(f"Total Months: {month_num}") 
print(f"Total: $ {net_total}")
print('Average  Change: $' + " {:07.2f}".format(avg))
print(f"Greatest Increase in Profits: {maxim_month} ($ {maxim})")
print(f"Greatest Decrease in Profits: {minim_month} ($ {minim})")

# writing to txt file
file_to_output = os.path.join("Analysis", "budget_analysis.txt")
a = "Financial Analysis"
b = "-----------------------------------------------------"
c = f"Total Months: {month_num}"
d = f"Total: $ {net_total}"
e = 'Average  Change: $ ' + "{:07.2f}".format(avg)
f = f"Greatest Increase in Profits: {maxim_month} ($ {maxim})"
g = f"Greatest Decrease in Profits: {minim_month} ($ {minim})"
n = '\n' 

output = f'{a} \n{b} \n{c} \n{d} \n{e} \n{f} \n{g}'
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
