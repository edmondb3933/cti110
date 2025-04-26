# Brandon Edmond
# 4/9/2025
# P1HW2
# Some basic math on numbers from inputs from users

# User input
budget = float(input("Enter budget: "))
destination = (input('Enter your travel desination: '))
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, ho wmuch do you need for food? "))
expenses = budget - (gas+accommodation+food)

# Adding expenses

print("----------Travel Expenses----------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("-----------------------------------")
print(f"{'Remaining Balance:':<20}${expenses:.2f}")
