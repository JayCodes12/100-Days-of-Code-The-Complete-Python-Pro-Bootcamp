print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15: "))
people = int(input("How many people to split the bill? "))

tip = tip /100
payment_amount = (bill / people) + ((bill/people) * tip)
print(f"You are paying ${payment_amount: .2f}")