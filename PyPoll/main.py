import os, sys
import csv

csvpath = os.path.join(r'C:\Users\Zhuoran Zhang\Desktop\election_data.csv')

votes = []          # A list to store the csv rows contents for easier looping and indexing.
candidates = []     # A list to store the name of unique candidates based on their order of appearance in csv. 
count = []          # A list to store the number of votes for each candidate
result = dict()     # A dictionary to establish a connection between the candidate name and the number of votes he/she gets.


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(row)       # Add csv rows into "votes" (list)
    
        if row[2] not in candidates:    # If a new candidate is found: add the name to "candidates" list
            candidates.append(row[2])
            count.append(1)             # Create a corresponding index to start counting the number of votes.
                                        # The "candidates" and the "count" lists share the same order of candidates            information
        else:
            count[int(candidates.index(row[2]))] += 1   # If this candidate already exists in "candidates" list, add one in                                                 his/her vote count. 
        

for i in range(len(candidates)):
    result[count[i]] = candidates[i]    # Populate the "result" dictionary. Votes:candidate as each key:value pair.

num_votes = len(votes)                  # The total number of votes = The total number of rows in csv.

print('Election Results')
print('-------------------------')
print('Total Votes:', num_votes)
print('-------------------------')


# This serves for ranking the candidates from high percentage to low.
# First sort the dict.keys (number of votes of candidates) in reverse order.
# Then print the name of candidate, percentage in 3 decimals and number of votes won.
for key in sorted(result.keys(), reverse=True): #reverse=True
    print(result[key] + ': ' + "{:.3%}".format(key/num_votes) + ' ('+ str(key)+ ')')

# Winner is the first key-value pair after reverse-order sorting.
winner_key = sorted(result.keys(), reverse=True)[0]

print('-------------------------')
print('Winner: ' + result[winner_key])
print('-------------------------')
    
with open('election_data_result.txt', 'w') as txt_file:
    
    sys.stdout = txt_file
    print('Election Results')
    print('-------------------------')
    print('Total Votes:', num_votes)
    print('-------------------------')


    for key in sorted(result.keys(), reverse=True): #reverse=True
        print(result[key] + ': ' + "{:.3%}".format(key/num_votes) + ' ('+ str(key)+ ')')

    winner = sorted(result.keys(), reverse=True)[0]

    print('-------------------------')
    print('Winner: ' + result[winner_key])
    print('-------------------------')




