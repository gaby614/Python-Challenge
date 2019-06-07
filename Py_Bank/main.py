# Import os module that has functions to interact with the file system
import os
# Import module for reading CSV files
import csv

#Get current working directory
mkdir = os.getcwd()
#Append file directory and make a complete file path
filepath = os.path.join( mkdir,'Resources','budget_data.csv')

#Initialize variables
mcount = 0 
total = 0 
PreValue = 0 
Diff = 0 
DiffMax = 0
DiffMin = 0 
revenue_change_total = 0.00
revenue_change_count = 0
#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     csv_row = next(csvreader)
     PreValue = int(csv_row[1])
     print(f'Financial Analysis'+'\n')
     print(f'---------'+'\n')
     print(csv_row[0], csv_row[1])
     for i in csvreader:
      
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue  
         revenue_change_total = revenue_change_total + Diff
         revenue_change_count = revenue_change_count + 1


         #Greatest increase in profits (financial analysis)
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         #Greatest decrease in profits (financial analysis)
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         # Number of total months (financial analysis)
         mcount = mcount + 1
         total += int(Amount) 

average_change = revenue_change_total / (revenue_change_count-1)

print(revenue_change_count)


#The total number of months included in the dataset
print(f'Total Months : {mcount}')
#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')
#The average of changes in "Profit/Losses" over the entire period
print(f'average_change: $ {average_change}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
# Greatest increase in profit
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')