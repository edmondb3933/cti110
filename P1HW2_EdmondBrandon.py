# Brandon Edmond
# 4/9/2025
# P1HW2
# Some basic math on numbers from inputs from users

# User input
budget = int(input("Enter budget"))
destination = (input('Enter your travel desination'))
gas = int(input("How much do you think you will spend on gas?"))
accommodation = int(input("Approximately, how much will you need for accomodation/hotel?"))
food = int(input("Last, ho wmuch do you need for food?"))
expenses = budget - (gas+accommodation+food)

# Adding expenses

print("----------Travel Expenses----------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")

print(f"Fuel: {gas}")
print(f"Accomodation: {accommodation}")
print(f"Food: {food}")
print(f"Remaining Blanace: {expenses}")