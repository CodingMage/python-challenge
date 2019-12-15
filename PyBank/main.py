import os, sys
import csv

csvpath = os.path.join(r'C:\Users\Zhuoran Zhang\Desktop\budget_data.csv')
contents = []
total = 0 
average = 0
profit = 0
profit_date = ''
loss = 0
loss_date = ''

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        contents.append(row)
        total += int(row[1])
    for i in range(len(contents)-1):
        change = int(contents[i+1][1])-int(contents[i][1])
        if profit < change:
            profit = change
            profit_date = contents[i+1][0]

        elif loss > change:
            loss = change
            loss_date = contents[i+1][0]

    average = (int(contents[-1][1])-int(contents[0][1]))/(len(contents)-1)


print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(contents)}')
print(f'total: {len(contents)}')

print('$ '+ str(total))
print(f'$ {round(average,2)}')

print(f'Greatest Increase in Profits: {profit_date} (${profit})')
print(f'Greatest Decrease in Profits: {loss_date} (${loss})')
    
with open('budget_data_results.txt', 'w') as txt_file:
    sys.stdout = txt_file
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {len(contents)}')
    #print(contents)
    print('$ '+ str(total))
    print(f'$ {round(average,2)}')

    print(f'Greatest Increase in Profits: {profit_date} (${profit})')
    print(f'Greatest Decrease in Profits: {loss_date} (${loss})')


#with open(output_path, 'w') as txt_file:
#    txt_file.write('Financial Analysis\n')
#    txt_file.write('----------------------------\n')
#    txt_file.write(f'Total Months: {len(contents)}\n')
#    txt_file.write('$ '+ str(total) + '\n')
#    txt_file.write(f'$ {round(average,2)}\n')
#    txt_file.write(f'Greatest Increase in Profits: {profit_date} (${profit})\n')
#    txt_file.write(f'Greatest Decrease in Profits: {loss_date} (${loss})\n')