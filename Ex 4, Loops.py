# admission prices 
BABY_PRICE = 0.00
CHILD_PRICE = 14.00
SENIOR_PRICE = 18.00
ADULT_PRICE = 23.00

#  age limits 
BABY_LIMIT = 2
CHILD_LIMIT = 12
SENIOR_LIMIT = 65

Number_of_visitors = int(input("Total number of visitors: "))
ages = []  # List to store ages
prices = []  # List to store prices

for i in range(Number_of_visitors):
    age = int(input(f"Enter the age for visitor {i + 1}: "))
    ages.append(age)

    if age < BABY_LIMIT:
        price = BABY_PRICE
    elif age <= CHILD_LIMIT:
        price = CHILD_PRICE
    elif age < SENIOR_LIMIT:
        price = ADULT_PRICE
    else:
        price = SENIOR_PRICE

    prices.append(price)
    print(f"Visitor {i + 1} (Age: {age}) - Price: ${price:.2f}")

print("\n--- Summary ---")
for i in range(Number_of_visitors):
    print(f"Visitor {i + 1}: Age {ages[i]}, Price ${prices[i]:.2f}")

total_revenue = sum(prices)
print(f"\nTotal revenue: ${total_revenue:.2f}")