## Import necessary packages
import pandas as pd
import json

## path to the files
filename = "Cs563ProjectFinalBenchmark.xlsx"
output = "output.json"

## Create dataframe from the excel file
df = pd.read_excel(filename)

## Initialization
bug_list = {}

## Looping through the rows
for idx, row in df.iterrows():
    bug = {'serial_number':row['serial_number'],
           'service':row['service'],
           'bug_link':row['bug_link'],
           'bug_type':row['bug_type'],
           'consider':row['consider'],
           'modified_file':'', 
           'modified_line_number':'',
           'comment':row['comment'],
           'buggyCommit':row['buggyCommit'],
           'fixedCommit':row['fixedCommit']}
    issue_num = row['bug_link'].rsplit('/',1)[1]
    service = row['service']
    bug_name = service+'_'+issue_num
    bug_list[bug_name] = bug

## Write to output json
with open(output,'w') as output_file:
    json.dump(bug_list,output_file)
