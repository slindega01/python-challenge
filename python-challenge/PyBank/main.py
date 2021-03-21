import csv

row_count = 0
net_total = 0
greatest_decrease = 0
greatest_increase = 0
net_total = 0
change = 0 

with open('../Resources/PyBank_Resource.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csvreader)
    for i in csv_reader:
        row_count += 1
        net_total = net_total + i[1]
        change = (int(i[1])+1) - int(i[1])
        average_per_change = change/len(csv_reader)
        average_change = average_change + average_per_change
        if int(i[1])>greatest_increase:
            greatest_increase = i[1]
        elif int(i[1])<greatest_decrease:
            greatest_decrease = int(i[1])
        else:
            continue 
            

print("Total Months: ", row_count)
print("Total: ", net_total)
print("Average Change: ", average_change)
print("Greatest Increase in Profits: ", greatest_increase)
print("Greatest Decrease in Profits: ", greatest_decrease)