#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv
import os

csvpath = os.path.join(".", "Resources", "election_data.csv")

output_results = os.path.join(".", "election_analysis.txt")

total_votes = 0

#counters
candidate_votes = {}
candidate_option = []

#winner
winning_candidate = ""
winning_count = 0

with open(csvpath) as election:
    reader = csv.reader(election)
    
    #skip header
    header = next(reader)
    #print(header)
   
  #loop through rows
    for row in reader:
        total_votes = total_votes +1
#     print(total_votes) 
        
    #telling where to find candidate name
        candidate_name = row[2]
        
        if candidate_name not in candidate_option:
           
            #loop through and find candidate names
            candidate_option.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1   



with open(output_results, "w") as txt_file:
    
    results = (
        f"Election Results\n"
        f"----------------------------\n" 
        f"Total Votes:{total_votes:,} \n"
        f"----------------------------\n")
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = votes / total_votes * 100
        results = results + f'{candidate}: {vote_percentage:.3f}% ({votes:,})\n'
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
    
    results = results + (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------------")
    
    print(results)

    txt_file.write(results)


# In[ ]:


# Election Results (format)
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

