totalCost = float(input("What is the cost of your dream home: "))
annual = float(input("What is your annual salary: "))
saved = float(input("What percent of your salary is saved: "))
semiRaise = float(input("What is your semi-annual-raise percentage: "))

downPayment = 0.25 * totalCost
savings = 0.0
rateR = 0.04
monthly = annual / 12
months = 0

while savings < downPayment:
    savings += savings * rateR / 12
    savings += saved * monthly
    months += 1

    if(months%6==0):
        annual = annual + semiRaise*annual
        monthly = annual/12

print("Number of months:", months)
