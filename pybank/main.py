#THIS CODE HAS BEEN DERIVED FROM BUT NOT LIMITED TO YOUTUBE, WWW3SCHOOL, ZOOM CLASS RECORDING ETC 
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")




# VARIABLES ARE BING INITILIZED 
total_months = 0
total_profit = 0
profit_changes = []
previous_profit = 0
greatest_increase = 0
greatest_decrease = 0
increase_date = ""
decrease_date = ""

# OPEN FILE BUDGET_DATA.CSV IN READING FORMAT 
with open(csvpath, "r") as file:
    reader = csv.reader(file)
    # THIS COMMAND IS TO SKIP THE FIRST ROW 
    next(reader)
    # FOR LOOP CREATED TO LOOP THROUGH EACH ROW 
    for row in reader:
        #  DATE AND PROFIT VARIABLES FOR /LOSS ARE BEING RECORDED 
        date = row[0]
        profit = int(row[1])
        # INCREMENT THE TOTAL MONTHS AND TOTAL PROFIT
        total_months += 1
        total_profit += profit
        # CALCULATE THE PROFT CHANGE AND APPEND TO THE LIST
        profit_change = profit - previous_profit
        profit_changes.append(profit_change)
        # UPDATE PREVIOUS PROFITS
        previous_profit = profit
        # IF STATMENT CREATED TO CHECK CHANGE IN PROFT INCREASE OR DECREASE 
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            increase_date = date
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            decrease_date = date

# REMOVE FIRST VALUE FROM THE LIST 
profit_changes.pop(0)
# CALCULATING AVERAGE FOR PROFIT
average_change = sum(profit_changes) / len(profit_changes)

# ANALYSIS OUT PUT TO THE TERMINAL 
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# EXPORT A TEXT FILE WITH RESULTS
output_path = "financial_analysis.txt"
with open(output_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------------------" + "\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit}\n")
    file.write(f"Average Change: ${round(average_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")
    file.close

