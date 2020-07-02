# main.py
# Resources/budget_data.csv analysis

import os
import csv

source_path = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("budget_data_analysis.txt")

with open (source_path, "r") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter = ',')
	for record in csv_reader:
		row_data = [{record[0]: int(record[1])} for record in csv_reader]
		diff = [list(row_data[i + 1].values())[0] - list(row_data[i].values())[0] for i in range(0, len(row_data) - 1)]
		
output = f'''Financial Analysis
----------------------------
Total Months: {len(row_data)}
Total: ${sum(list(row_data[i].values())[0] for i in range(0, len(row_data)))}
Average Change: ${round(sum(diff)/len(diff), 2)}
Greatest Increase in Profits: {list(row_data[diff.index(max(diff))+ 1].keys())[0]} (${max(diff)})
Greatest Decrease in Profits: {iter(row_data[diff.index(min(diff))+ 1].keys()).__next__()} (${min(diff)})
'''

print(output)

with open (output_file, "w") as handle:
	handle.write(output)


	





