# Getting user input for the base and exponent for the first part
print(f"-----Calculating Exponents----")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the base value: "))

# Calculating the result
result = base ** exponent

# Printing the output with the base, exponent, and result
print(f"{base} raised to the power of {exponent} is {result} !!")

# Getting three integers from the user for the second part

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))
num4 = int(num1 + num2 - num3)

# Printing the output with the starting, added and subtracted integer and result
print(f"{num1} + {num2} - {num3} is equal to {num4}" )