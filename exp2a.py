def calculate_gross_salary():
    # Get user input for Basic Salary
    bs = float(input("Enter the Basic Salary (BS): "))

    # Calculate allowances
    da = 0.70 * bs  # 70% of BS
    ta = 0.30 * bs  # 30% of BS
    hra = 0.10 * bs  # 10% of BS

    # Calculate Gross Salary
    gross_salary = bs + da + ta + hra

    # Display the results
    print("\n--- Salary Breakdown ---")
    print(f"Basic Salary (BS): {bs:.2f}")
    print(f"Dearness Allowance (DA): {da:.2f}")
    print(f"Travel Allowance (TA): {ta:.2f}")
    print(f"House Rent Allowance (HRA): {hra:.2f}")
    print(f"Gross Salary: {gross_salary:.2f}")

# Run the function
calculate_gross_salary()
