# main.py
# Resources/election_data.csv tabulation

import os
import csv
from operator import itemgetter

source_path = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("election_results.txt")

def vote_count(source):
	candidates = {"Correy": 0,
				"Khan": 0,
				"Li": 0,
				"O'Tooley": 0
				}

	with open(source, "r") as election_data:
		votes = csv.reader(election_data, delimiter = ",")
		next(votes)
		for vote in votes:
			if vote[2] == "Khan":
				candidates["Khan"] += 1
			elif vote[2] == "Correy":
				candidates["Correy"] += 1
			elif vote[2] == "Li":
				candidates["Li"] += 1
			elif vote[2] == "O'Tooley":
				candidates["O'Tooley"] += 1
				
		total_votes = sum(votes for votes in candidates.values())
		# dict.items() returns a list of k, v, tuple pairs
		res = sorted(candidates.items(), key=itemgetter(1), reverse=True)
			
		results = f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{res[0][0]}: {res[0][1]/total_votes:.3%} ({res[0][1]})
{res[1][0]}: {res[1][1]/total_votes:.3%} ({res[1][1]})
{res[2][0]}: {res[2][1]/total_votes:.3%} ({res[2][1]})
{res[3][0]}: {res[3][1]/total_votes:.3%} ({res[3][1]})
-------------------------
Winner: {max(candidates, key=candidates.get)}
-------------------------
'''	
	with open(output_file, "w") as handle:
		handle.write(results)
		
	print(results)
				
vote_count(source_path)
				

							

		
		

