totalCost = float(input("What is the cost of your dream home: "))
annual = float(input("What is your annual salary: "))
saved = float(input("What percent of your salary is saved: "))

downPayment = 0.25 * totalCost
savings = 0.0
rateR = 0.04
monthly = annual / 12
months = 0

while savings < downPayment:
    savings += savings * rateR / 12
    savings += saved * monthly
    months += 1

print("Number of months:", months)
