import os
import csv
print("Financial Analysis")
print("----------------------------")
find_csv = "/Users/christineyang/Desktop/challenge3/python-challenge/PyBank/Resources/budget_data.csv"
month = 0
profit_loss = 0
profit_list = []
month_list = []
value = 0 
with open(find_csv, "r") as open_file:
    reader = csv.reader(open_file, delimiter=",")
    next(open_file, None)
    for row in reader:
        month += 1
        profit_loss += int(row[1])
        profit_list.append(row[1])
        month_list.append(row[0]) 
    
    
    print("Total Months: " + str(month))
    print("Total: $" +str(profit_loss))
    # print(int(profit_list[month-1]))
    # print(int(profit_list[0]))
    change = int(profit_list[month-1]) - int(profit_list[0])
    change_average = round((change / month), 2)
    print("Average Change: $" + str(change_average))

value = 0
i = 1
while i <= int(month - 1):

    compare_big = int(profit_list[i]) - int(profit_list[i-1])
    if value > compare_big:
        value = value
    elif compare_big > value :
        value = compare_big
        date = month_list[i]
    i += 1
print("Greatest Increase in Profits: " + date + " ($" + str(value) + ")")
svalue = 0
j = 1
while j <= int(month - 1):

    small = int(profit_list[j]) - int(profit_list[j-1])
    if svalue < small:
        svalue = svalue
    elif small < svalue :
        svalue = small
        sdate = month_list[j]
    j += 1


print("Greatest Decrease in Profits: " + sdate + " ($" + str(svalue) + ")")

a = "/Users/christineyang/Desktop/challenge3/python-challenge/PyBank/analysis"
write_path = os.path.join(a, "PyBank.txt")
lines = ["Financial Analysis","----------------------------","Total Months: " + str(month),
    "Total: $" +str(profit_loss),"Average Change: $" + str(change_average),
    "Greatest Increase in Profits: " + date + " ($" + str(round(value, 0)) + ")",
     "Greatest Decrease in Profits: " + sdate + " ($" + str(svalue) + ")"]
with open(write_path, "w") as f:
    f.write("\n".join(lines))
    f.close()
   



