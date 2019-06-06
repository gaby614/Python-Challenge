# Import os module that has functions to interact with the file system
import os
# Import module for reading CSV files
import csv

#Get current working directory
mkdir = os.getcwd()
#Append file directory and make a complete file path
filepath = os.path.join( mkdir,'Resources','budget_data.csv')

#Initialize variables
mcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0; rev_change = 0; rev_change_list = []; mo_of_change = []

#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'---------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue

   #       #changes of revenue calculations
   #       rev_change = int(row["Revenue"]) - PreValue
   #       PreValue = int(row["Revenue"])
   #       mo_of_change = mo_of_change + [row["Date"]]

   #       #print the outcomes
   # output = (
   #       f"Total Months: {Month}\n"
   #       f"Total Revenue: {Amount}\n"
   #       f"Average Revenue Change: ${revenue_avg}\n"
   #       f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
   #       f"Greatest decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}\n"
   #        )

   # print(output)
        
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

         # #calculate average_change
         # average_change = round(total/month, 2)

  
#The total number of months included in the dataset
print(f'Total Months : {mcount}')
#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')
# #The average of changes in "Profit/Losses" over the entire period
# print(f'Total: $ {total}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
# Greatest increase in profit
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')