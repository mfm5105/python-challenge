#first we will import os module to allow us to create file paths accross systems
import os

#import module to read csv files
import csv

#files to load and output
file_input=os.path.join("Resources","budget_data.csv")


#creating variables

#open csv file
with open(file_input) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

#skipping header
    csv_header=next(csvreader)
 #starting from the first row   
    total_months=0
    net_total_amount=0
    monthly_change=0
    monthly_change_list=[]
    current_month=0
    previous_month=867884
    average=0
    date_list=[]
    greatest_increase_profit=0
    greatest_decrease_losses=0

    #loops
    for row in csvreader:
        #tracking the total of months
        total_months +=1
        net_total_amount +=int(row[1])

        #tracking monthly change
        current_month=row[1]
        monthly_change= float(current_month)-float(previous_month)
        previous_month=row[1]
        monthly_change_list.append(monthly_change)
        date_list.append(row[0])
        #tracking greatest increase profit
        greatest_increase_profit= max(monthly_change_list)
        max_date_index=monthly_change_list.index(greatest_increase_profit)
        max_date=date_list[max_date_index]

        #mtracking greatest decrease profit
        greatest_decrease_profit= min(monthly_change_list)
        min_date_index=monthly_change_list.index(greatest_decrease_profit)
        min_date=date_list[min_date_index]

    average=sum(monthly_change_list)/(total_months-1)

#gitbash 
print("---------------------------Financial Analysis ----------------------------")
print("Total Months:"+ str(total_months))
#printing total 
print("Total:$"+ str(net_total_amount))
print("Average Change: $"+ str(average))
print("Greatest Increase in Profits:"+ str(max_date) + "(" +str(greatest_increase_profit)+")")
print("Greatest Decrease in Profits:"+ str(min_date) + "(" +str(greatest_decrease_profit)+")")
print("--------------------------------------------------------------------------")

# output to a text file
file_output=os.path.join("analysis","budget_analysis.txt")
with open(file_output, "w", newline="") as exportfile:
    exportfile.write("Financial Analysis"+ "\n")
    exportfile.write("Total Months: "+ str(total_months)+"\n")
    exportfile.write("Total: "+ "$"+str(net_total_amount)+"\n")
    exportfile.write("Greatest Increase in Profits:"+ str(max_date) +"("+ str(greatest_increase_profit) + ")"+"\n")
    exportfile.write("Greatest Decrease in Profits:"+ str(min_date) +"("+str(greatest_decrease_profit)+ ")"+"\n")
    exportfile.write("--------------------------------------------------------------------------\n")
