Here’s a complete Python program based on your assignment instructions. You can copy this code into any Python IDE or text editor and run it.
# Brandon Edmond
# 4/18/25
# P2LAB2
# Using a dictionary to store user input and display output to user

# Creating the dictionary with car models as keys and MPG as values
car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get the keys from the dictionary
keys = car_mpg.keys()
print("Available vehicles:", keys)

# Prompt user for vehicle input
vehicle = input("Enter a vehicle to see it's mpg: ")

# Check if vehicle exists in dictionary
if vehicle in car_mpg:
    mpg = car_mpg[vehicle]
    print(f"The {vehicle} iets {mpg} mpg.")
    
    # Prompt user for miles they plan to drive
    try:
        miles = float(input("Enter the number of miles you will drive the vehicle: "))
        
        # Calculate gallons of gas needed
        gallons_needed = miles / mpg
        
        # Display result rounded to two decimal places
        print(f" {gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
    except ValueError:
        print("Please enter a valid number for miles.")
else:
    print("The vehicle you entered is not in the list. Please check your spelling and try again.")