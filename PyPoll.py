# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join(r"C:/Users/antba/OneDrive/Desktop/Module_3_Election_analysis/Election_Analysis/Resources/election_results.csv")
# Add a variable for file to save path
file_to_save = os.path.join(r"C:/Users/antba/OneDrive/Desktop/Module_3_Election_analysis/Election_Analysis/Analysis/election_results.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
