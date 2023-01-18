#!/usr/bin/env python
# coding: utf-8

# In[3]:




#create file path
import os

#read csv file
import csv

csvpath = os.path.join(".", 'budget_data.csv')

#output
output_analysis = os.path.join("..",  "bank_budget_analysis.txt")

# set values
total_months = 0
total_net = 0
net_change_list = []
highest_profit = ["", 0]
lowest_profit = ["", 0]

# open CSV file
with open("budget_data.csv") as file:
    
    # read CSV file
    reader = csv.reader(file, delimiter=',')
    
    # skip the header
    next(reader)
   
    # for loop
    for row in reader:
        
        # sum the months
        total_months += 1
       
        # add the net amount to the total net
        total_net += int(row[1])
        
        # calculate the net change
        if total_months > 1:
            net_change = int(row[1]) - previous_net
            net_change_list.append(net_change)
            
            
            # find the month with the greatest & lowest change
            if net_change > highest_profit[1]:
                highest_profit[0] = row[0]
                highest_profit[1] = net_change
            elif net_change < lowest_profit[1]:
                lowest_profit[0] = row[0]
                lowest_profit[1] = net_change
       
        # save the current net amount as the previous net amount
        previous_net = int(row[1])

# calculate the average net change
average_change = sum(net_change_list) / (total_months - 1)


   
    # print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net:,}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {highest_profit[0]} (${highest_profit[1]:,})")
print(f"Greatest Decrease in Profits: {lowest_profit[0]} (${lowest_profit[1]:,})")

with open(output_analysis, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {highest_profit[0]} (${highest_profit[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {lowest_profit[0]} (${lowest_profit[1]})\n")


# In[ ]:




