import os
import csv
from collections import Counter

#cwd=os.getcwd()
#files=os.listdir(cwd)
#print(files)

total_votes = 0
candidates_list=[]
count=0

infile = os.path.join('Resources', 'election_data.csv')
outfile = os.path.join('analysis', 'election_analysis.txt')

with open(infile, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    title = next(csv_reader)
    #print(title)

    for row in csv_reader:
        
        total_votes=total_votes+1
        
        candidates=row[2]
        if candidates not in candidates_list:
            candidates_list.append(candidates)             
            for candidates in candidates_list:
                print(candidates_list)
        
    if candidates=='Charles Casper Stockham':
        count+=1
        print(max(count))
    
       
    
     
        
       


with open(outfile,'w') as text_file:
    output=(
        f'Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'-------------------------\n'
        )
    print(output)
    text_file.write(output)

