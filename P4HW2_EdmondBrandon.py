# Brandon Edmond

# 4/26/25

# P4HW2

# This code calculates gross pay for multiple employees determined by the user and total amount of paid overtime.
 
def calculate_employee_pay():
    # Totals to track across all employees
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    employee_count = 0

    while True:
        # Ask for employee name
        name = input("Enter the employee's name (or type 'Done' to finish): ")
        if name.lower() == "done":
            break

        # Get hours worked and pay rate
        try:
            hours_worked = float(input(f"Enter the number of hours {name} worked this week: "))
            pay_rate = float(input(f"Enter {name}'s hourly pay rate: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for hours and pay rate.\n")
            continue

        # Initialize values
        regular_hours = 40
        overtime_hours = 0
        overtime_pay = 0

        # Calculate pay
        if hours_worked > regular_hours:
            overtime_hours = hours_worked - regular_hours
            overtime_pay = overtime_hours * (pay_rate * 1.5)
            regular_pay = regular_hours * pay_rate
        else:
            regular_pay = hours_worked * pay_rate

        gross_pay = regular_pay + overtime_pay

        # Update totals
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        employee_count += 1

        # Display individual summary
        print("\n--- Employee Pay Summary ---")
        print(f"Employee Name      : {name}")
        print(f"Pay Rate           : ${pay_rate:.2f}")
        print(f"Hours Worked       : {hours_worked}")
        print(f"Overtime Hours     : {overtime_hours}")
        print(f"Overtime Pay       : ${overtime_pay:.2f}")
        print(f"Regular Pay        : ${regular_pay:.2f}")
        print(f"Gross Pay          : ${gross_pay:.2f}\n")

    # Final totals summary
    print("\n========== Payroll Summary ==========")
    print(f"Total Employees Processed : {employee_count}")
    print(f"Total Overtime Pay        : ${total_overtime_pay:.2f}")
    print(f"Total Regular Pay         : ${total_regular_pay:.2f}")
    print(f"Total Gross Pay           : ${total_gross_pay:.2f}")
    print("=====================================")

# Run the program
calculate_employee_pay()

