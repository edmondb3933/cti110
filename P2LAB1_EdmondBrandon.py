# Brandon Edmond
# 4/18/25
# P2LAB1
# code that performs mathematical calculations and displays information to users

# Use an approximate value for pi
pi = 3.14159

# Get radius from the user
radius = float(input("What is the radius of the circle? "))

# Calculations
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * (radius ** 2)

# Output: Display formatted results
print("\n------- Circle Calculations -------")
print(f"{'The diameter of the circle is ':<15}{diameter:.1f}")
print(f"{'The circumference of the circle is ':<15}{circumference:.2f}")
print(f"{'The area of the circle is ':<15}{area:.3f}")