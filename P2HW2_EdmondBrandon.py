# Brandon Edmond
# 4/18/25
# P2HW2
# This code collects test grades for six modules, stores them in a list displaying the lowest, highest, sum, and average of the grades.

# Pseudocode:
# 1. Prompt the user to enter grades for Module 1 through Module 6 (each separately).
# 2. Store each entered grade in a list.
# 3. Calculate the lowest grade using min().
# 4. Calculate the highest grade using max().
# 5. Calculate the sum of the grades using sum().
# 6. Calculate the average by dividing the sum by the number of grades.
# 7. Display the results in a formatted and spaced manner with average shown to two decimal places.

# Input: Collecting grades
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store in list
module_grades = [module1, module2, module3, module4, module5, module6]

# Processing
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Output
print("\n---------- Grade Summary ----------")
print(f"{'Lowest Grade:':<20}{lowest}")
print(f"{'Highest Grade:':<20}{highest}")
print(f"{'Sum of Grades:':<20}{total}")
print(f"{'Average:':<20}{average:.2f}")
