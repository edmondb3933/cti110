# Brandon Edmond
# 4/26/25
# P4HW1
# This code collects test grades for six modules, stores them in a list displaying the lowest, highest, sum, and average of the grades.

# Ask how many scores the user wants to enter
num_scores = int(input("How many module scores would you like to enter? "))

# Initialize list to store valid scores
valid_scores = []

# Collect scores with validation
for i in range(1, num_scores + 1):
    while True:
        try:
            score = float(input(f"Enter score for Module {i}: "))
            if 0 <= score <= 100:
                valid_scores.append(score)
                break
            else:
                print("Invalid input. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Processing
lowest_score = min(valid_scores)
modified_scores = valid_scores.copy()
modified_scores.remove(lowest_score)

average = sum(modified_scores) / len(modified_scores)

# Determine letter grade
if average >= 90:
    letter = 'A'
elif average >= 80:
    letter = 'B'
elif average >= 70:
    letter = 'C'
elif average >= 60:
    letter = 'D'
else:
    letter = 'F'

# Output
print("\n---------- Grade Summary ----------")
print(f"{'Lowest Score:':<25}{lowest_score}")
print(f"{'Scores (lowest dropped):':<25}{modified_scores}")
print(f"{'Average of Remaining Scores:':<25}{average:.2f}")
print(f"{'Letter Grade:':<25}{letter}")

