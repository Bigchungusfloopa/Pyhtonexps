def factorial_iterative(n):
    """Calculates factorial using iteration."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculates factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Get user input
try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"\nFactorial of {n} (Iterative): {factorial_iterative(n)}")
        print(f"Factorial of {n} (Recursive): {factorial_recursive(n)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
