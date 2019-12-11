import os, sys
import csv

csvpath = os.path.join(r'C:\Users\Zhuoran Zhang\Desktop\election_data.csv')
print(csvpath)

votes = []
candidates = []
count = []
result = dict()


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(row)
    
        if row[2] not in candidates:
            candidates.append(row[2])
            count.append(1)
        else:
            count[int(candidates.index(row[2]))] += 1
        

for i in range(len(candidates)):
    result[count[i]] = candidates[i]

num_votes = len(votes)

print('Election Results')
print('-------------------------')


for key in sorted(result.keys(), reverse=True): #reverse=True
    print(result[key] + ': ' + "{:.3%}".format(key/num_votes) + ' ('+ str(key)+ ')')

winner = sorted(result.keys(), reverse=True)[0]

print('-------------------------')
print('Winner: ' + result[winner])
print('-------------------------')
    
with open('election_data_result.txt', 'w') as txt_file:
    
    sys.stdout = txt_file
    print('Election Results')
    print('-------------------------')


    for key in sorted(result.keys(), reverse=True): #reverse=True
        print(result[key] + ': ' + "{:.3%}".format(key/num_votes) + ' ('+ str(key)+ ')')

    winner = sorted(result.keys(), reverse=True)[0]

    print('-------------------------')
    print('Winner: ' + result[winner])
    print('-------------------------')




