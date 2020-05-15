#write a program to calculate how many months it will take to save enough money
#to buy dreamed house

total_cost = float(input('Cost of the house: '))
portion_down_payment = 0.25*total_cost
annual_salary = float(input('Annual salary: '))
monthly_salary = annual_salary/12
portion_saved = float(input('Percent of your monthly salary to be saved: '))

r = 0.04
current_savings = 0
i = 0

while current_savings < portion_down_payment:
    i += 1
    current_savings += current_savings*(r/12) + monthly_salary*portion_saved
  
print(i)
