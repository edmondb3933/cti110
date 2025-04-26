# Make a time table for user input

def show_multiplication_table(number):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):  # For loop used here
        print(f"{number} x {i} = {number * i}")

# Main loop
run_again = "yes"
while run_again.lower() == "yes":  # While loop used here
    try:
        num = int(input("Enter an integer: ")) # User input
        if num >= 0:
            show_multiplication_table(num)
        else:
            print("Cannot accept negative values.")
    except ValueError:
        print("Please enter a valid integer.")

    run_again = input("\nDo you want to run the program again? (yes/no): ")

print("Goodbye!")
