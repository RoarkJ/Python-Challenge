# main.py
# Resources/election_data.csv tabulation

# Import Dependencies
import os
import csv
import sys
from operator import itemgetter

# Create variable holding path to source csv file "Resources" is the folder
# holding the "election_data.csv" file.  So, join these to create relative path.
source_path = os.path.join("Resources", "election_data.csv")
# Create varaible holding path to create results text document
output_file = os.path.join("election_results.txt")
# Provide container structure containing candidate names and coresponding vote count
# I could have started with an empty dictionary and added each candidate as I came across
# them in the results but, in an election one typically will know all candidates
# ahead of time.  Also, defining all candidates provides a way to make sure each vote 
# is going to a valid candidate.
candidates = {"Correy": 0, "Khan": 0, "Li": 0, "O'Tooley": 0}

# Implement function with parameters to recieve needed arguments
# Design the function to handle any number of candidates
def vote_count(source, candidates, output):
	# open source file using the with statement to handle cleanup
	with open(source, "r") as election_data:
		# Create csv.reader object and associate to a variable.
		votes = csv.reader(election_data, delimiter = ",")
		# Bypass the header data
		next(votes)
		
		# create loop to go through each vote list containing 
		# vote data for a single vote in the csv reader object "votes"
		for vote in votes:
			candidate=vote[2]
			# Implement try|except block to handle possible candidate error in source data
			# candidates is an empty dictionary at this point {}
			# if key in dictionary: 
			#	dictionary[key]+=1
			# else: (implicitly key is not in dictionary, aka first record)
			# 	dictionary[key]=1
			try:
				# read each line of data and assign vote to appropriate candidate
				candidates[candidate]+=1
				# If there is a candidate mismatch hadle the error gracefully
				# catch error and send message to 
				# notifying election official of error and stop the vote count
			except:
				sys.exit('Probable Candidate Reference Error!')
				
		# Calculate grand total votes from candidate totals
		total_votes = sum(tally for tally in candidates.values())
		# Sort the candidates based on votes received by each candidate
		# Order greatest to least candidate vote count
		# dict.items() returns a list of k, v, tuple pairs
		# I can always use a lambda expression as the value of the key
		# but using built-ins is faster processing.
		res_ord = sorted(candidates.items(), key=itemgetter(1), reverse=True)
		# Create a list to hold f-string elements that describe the results for each candidate
		res_output=[]
		
		# Implement for loop to produce the f-string for each candidate
		# and append the resut to the res_output list 
		for i in range(0, len(res_ord)):
			res_output.append(f'{res_ord[i][0]}: {res_ord[i][1]/total_votes:.3%} ({res_ord[i][1]})')
		# Join the individual candidate results f-string into 
		# one long string with new line formatting creating
		# desired results output text
		# join() method takes an iterable and joins it's elements
		# into one string preserving element format.
		results_j = '\n'.join(res_output)
		
		# Create desired results output text structure with the results-join
		# inserted into desired location within the results text structure
		results = f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{results_j}
-------------------------
Winner: {max(candidates, key=candidates.get)}
-------------------------
'''	
	# Produce the output file and place in the appropriate directory
	# Use with statement to do cleanup after action completes
	with open(output_file, "w") as handle:
		handle.write(results)
	# Print the election results to terminal for perusal
	print(results)
# Call the function I created above with the appropriate arguments
vote_count(source_path, candidates, output_file)
				

