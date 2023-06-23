totalCost = 1000000
downPayment = 0.25*totalCost
semiAnnualRaise = 0.07
returnRate = 0.04
months = 36

def calc(salary):
    low = 0
    high = 10000
    steps = 0

    while low <= high:
        steps += 1
        rate = (low + high) // 2 / 10000
        currentSal = salary
        savings = 0

        for month in range(1, months+1):
            savings += currentSal * rate / 12
            savings += savings * returnRate / 12
            if month % 6 == 0:
                currentSal += currentSal * semiAnnualRaise

        if abs(savings - downPayment) <= 100:
            return rate, steps
        elif savings < downPayment:
            low = rate * 10000 + 1
        else:
            high = rate * 10000 - 1

    return None, steps


salary = float(input("Enter your starting salary: "))

savingsRate, numOfSteps = calc(salary)

if savingsRate is not None:
    print("Best savings rate:", savingsRate)
    print("Steps in bisection search:", numOfSteps)
else:
    print("It is not possible to save for the down payment in 36 months.")
