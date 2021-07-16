# main.py
# Resources/budget_data.csv analysis

# Import Dependencies
import os
import csv

# Create variable holding path to source csv file
source_path = os.path.join("Resources", "budget_data.csv")
# Create varaible holding path to create results text document
output_file = os.path.join("budget_data_analysis.txt")

# open source file using the "with" statement to handle cleanup
with open (source_path, "r") as csvfile:
	# Create csv.reader object and assign it a variable.
	csv_reader = csv.reader(csvfile, delimiter = ',')
	# Bypass the header data
	next(csv_reader)
	# Using a list comprehension go through each record creating a list of dictionaries
	# holding the key value pairs for date=key and profit/loss=value
	row_data = [{record[0]: int(record[1])} for record in csv_reader]
	# Create another list comprehension to determine the difference in 
	# profit loss from month to month and store resulting data in a list
	# and associate the list with a variable.
	diff = [list(row_data[i + 1].values())[0] - list(row_data[i].values())[0] for i in range(0, len(row_data) - 1)]

# Create desired output text structure with the results 
# inserted into desired locations within the results text structure
# Line 35 and 36 do the exact same thing. Just example of two ways to accomplish the same task.
output = f'''Financial Analysis
----------------------------
Total Months: {len(row_data)}
Total: ${sum(list(row_data[i].values())[0] for i in range(0, len(row_data)))}
Average Change: ${round(sum(diff)/len(diff), 2)}
Greatest Increase in Profits: {list(row_data[diff.index(max(diff))+ 1].keys())[0]} (${max(diff)})
Greatest Decrease in Profits: {iter(row_data[diff.index(min(diff))+ 1].keys()).__next__()} (${min(diff)})
'''
# Print the budget analysis results to terminal for perusal
print(output)

# Produce the output file and place in the appropriate directory
# Use "with" statement to handle cleanup after action completes
with open (output_file, "w") as handle:
	handle.write(output)


	





