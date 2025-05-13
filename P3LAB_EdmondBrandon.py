def money_breakdown():
    # Get input from the user
    amount = float(input("Enter an amount of money (e.g., 2.75): $"))

    # Convert the amount to cents to avoid floating point precision issues
    cents = round(amount * 100)

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
    for coin, count in coin_count.items():
        # For Plural
        if count == 1:
            print(f"{count} {coin}")
        else:
            if coin == "penny":
                print(f"{count} pennies")
            else:
                print(f"{count} {coin}s")

# Run the program
money_breakdown()