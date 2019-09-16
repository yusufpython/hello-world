#a program that calculate how many month it will take a user to buy house in Bay area
annual_salary=float(input("enter your annual salary:"))
portion_down_payment=float(input("enter the percentage of your salary to save, as a decimal:"))
total_cost=float(input("enter the cost of your dream house:"))
monthly_salary=annual_salary/12
portion_saved=(portion_down_payment*monthly_salary/100)

#annual rate return, i assumed the percentage to be 0

#the current saving, the intial saving is zero having a return value and portion saved
current_savings=0
number_month=current_savings+total_cost/portion_saved
print("numbers of month is:",number_month)