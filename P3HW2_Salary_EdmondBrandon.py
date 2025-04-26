def calculate_employee_pay():
    # Get input from the user
    name = input("Enter the employee's name: ")
    hours_worked = float(input("Enter the number of hours worked this week: "))
    pay_rate = float(input("Enter the employee's hourly pay rate: "))

    # Define regular work hours
    regular_hours = 40
    overtime_hours = 0
    overtime_pay = 0

    # Check for overtime
    if hours_worked > regular_hours:
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = regular_hours * pay_rate
    else:
        regular_pay = hours_worked * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Display the results
    print("\n--- Employee Pay Summary ---")
    print(f"Employee Name      : {name}")
    print(f"Pay Rate           : ${pay_rate:.2f}")
    print(f"Hours Worked       : {hours_worked}")
    print(f"Overtime Hours     : {overtime_hours}")
    print(f"Overtime Pay       : ${overtime_pay:.2f}")
    print(f"Regular Pay        : ${regular_pay:.2f}")
    print(f"Gross Pay          : ${gross_pay:.2f}")

# Run the program
calculate_employee_pay()
