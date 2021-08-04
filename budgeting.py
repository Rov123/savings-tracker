#creating my variables
pay_per_hour = float(input("Hourly rate"))
hours_a_week = float(input("hours worked in a week"))
bills = float(input("amount due for bills"))
clothing = float(input("amount expected to be spent on clothes"))
food = float(input("amount spent on food a month"))
entertainment = float(input("money to be spent on entertainment"))
travel = float(input("amount to be spent on travel "))
 
total = [pay_per_hour,hours_a_week,bills,clothing,food,entertainment,travel]


def calculate(total):
    expenses = bills + clothing +food +travel+ entertainment
    weeks_pay = pay_per_hour * hours_a_week
    months_pay = weeks_pay * 4
    pay_left = months_pay - expenses
    return pay_left

print("You have " , calculate(total), "left")