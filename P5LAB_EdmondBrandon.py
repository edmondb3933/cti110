# Brandon Edmond
# 5/5/25
# P5LAB
# Simulate a customer using a self-checkout machine

import random

def disperse_change(change):
    # Convert the amount to cents to avoid floating point precision issues
    cents = round(change * 100)

    # Dictionary to store coin values in cents
    coin_values = {
        "dollar": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }

    # Dictionary to store the coin count
    coin_count = {}

    for coin, value in coin_values.items():
        count = cents // value
        if count > 0:
            coin_count[coin] = count
            cents -= count * value

    # Display results
    print("Change to return:")
    for coin, count in coin_count.items():
        if count == 1:
            print(f"{count} {coin}")
        else:
            if coin == "penny":
                print(f"{count} pennies")
            else:
                print(f"{count} {coin}s")

def main():
    # Generate a random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    # Get the amount paid by the customer
    amount_paid = float(input("How much cash will you put in the self-checkout?"))

    # Check if amount paid is sufficient
    if amount_paid < total_owed:
        print("Not enough money provided.")
    else:
        # Calculate the change to be returned
        change = round(amount_paid - total_owed, 2)
        print(f"Change is: ${change:.2f}")
        disperse_change(change)

# Run the program
if __name__ == "__main__":
    main()