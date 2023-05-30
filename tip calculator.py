print("Welcome to Berto tip calculator")
bill =int(input("Enter the bill?"))
tip = int(input("Enter the percentage of tip you want to pay 10,12 or 15?"))
people=int(input("How many people to split the bill?"))

totalTip=(tip/100)+1
totalBill=(bill/people) * totalTip
finalBill=round(totalBill,3)

print(f"Each person will pay {finalBill} amount")
