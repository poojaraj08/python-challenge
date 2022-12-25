import csv 
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read in CSV file
csv_data_path = os.path.join("Resources", "budget_data.csv")
print(csv_data_path)

#Assigns index value to variables for each column
MONTH_INDEX = 0
PROFIT_INDEX = 1
#Reads in CSV file
with open(csv_data_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)

    #initializing variables
    month_count = 0
    total_sum = 0
    total_profit = 0
    total_loss = 0
    changes = []
    prev_value = None
    greatest_increase_value = 0
    greatest_decrease_value = 0
    greatest_increase_date = None
    greatest_decrease_date = None
#Loop that iterates through the rows of file
 
    for row in csvreader:
        profit = int(row[PROFIT_INDEX])
        #  incrementing month count
        month_count = month_count + 1
        total_sum = total_sum + profit
        change = 0
        #Building month to month profit change list
         #First loop will not have value for prev_value; every subsequent loop will compare to previous value
        if(prev_value != None):
            change = profit - prev_value
            changes.append(change)
        #Setting current value to prev_value for next iteration in loop    
        prev_value = profit
        #Calculating the running max:
        # If the profit change is greater than zero, then we will compare the profit change to the running max to determine if
        #there is a new max.
        if(profit > 0):
            if(change > greatest_increase_value):
                greatest_increase_value = change
                greatest_increase_date = row[MONTH_INDEX]
        #Calculating the running min:
        # If the profit change is less than zero, then we will compare the profit change to the running min to determine if
        #there is a new min.
        if(profit < 0):
            if(change < greatest_decrease_value):
                greatest_decrease_value = change
                greatest_decrease_date = row[MONTH_INDEX]
   # Once we have the list of profit changes, we will find the average of those changes.
    avg_change = sum(changes)/(int(month_count) - 1)
    #Printing results of all calculations.
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months:{str(month_count)}")
    print(f"Total: ${str(total_sum)}")
    print(f"Average Change: ${str(round(avg_change, 2))}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} ({str(greatest_increase_value)})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} ({str(greatest_decrease_value)})")
    #Exporting to text file
    with open('Analysis/pybank.txt', 'a') as pb:
        pb.write("Financial Analysis" + "\n")
        pb.write("----------------------------" + "\n")
        pb.write(f"Total Months:{str(month_count)}" + "\n")
        pb.write(f"Total: ${str(total_sum)}" + "\n")
        pb.write(f"Average Change: ${str(round(avg_change, 2))}" + "\n")
        pb.write(f"Greatest Increase in Profits: {greatest_increase_date} ({str(greatest_increase_value)})" + "\n")
        pb.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ({str(greatest_decrease_value)})" + "\n")



