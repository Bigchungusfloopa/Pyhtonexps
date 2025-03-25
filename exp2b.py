def arithmetic_operations():
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Undefined (Division by zero)"
    modulus = num1 % num2 if num2 != 0 else "Undefined (Modulus by zero)"

    # Display results
    print("\n--- Arithmetic Operations ---")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} × {num2} = {multiplication}")
    print(f"{num1} ÷ {num2} = {division}")
    print(f"{num1} % {num2} = {modulus}")

# Run the function
arithmetic_operations()
