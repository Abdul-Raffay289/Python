# ----------------------------------------------------------------------
# Simple Addition and Subtraction Application
# This script defines two basic arithmetic functions and demonstrates 
# how to use them within a simple command-line interface.
# ----------------------------------------------------------------------

def add(a, b):
    """
Adds two numbers, a and b.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number (b) from the first number (a).

    Args:
        a (float): The number to subtract from (minuend).
        b (float): The number to be subtracted (subtrahend).

    Returns:
        float: The difference between a and b.
    """
    return a - b

def run_cli_tests():
    """
    Runs a few sample calculations and prints the results.
    This serves as a simple command-line test interface.
    """
    print("--- Simple Calculator Demo ---")

    # --- Addition Examples ---
    num1_add = 15
    num2_add = 7.5
    result_add = add(num1_add, num2_add)
    print(f"\nAddition Test:")
    print(f"Adding {num1_add} and {num2_add}: {result_add}") # Expected: 22.5

    num3_add = -10
    num4_add = 3
    result_add_neg = add(num3_add, num4_add)
    print(f"Adding {num3_add} and {num4_add}: {result_add_neg}") # Expected: -7

    # --- Subtraction Examples ---
    num1_sub = 50
    num2_sub = 18
    result_sub = subtract(num1_sub, num2_sub)
    print(f"\nSubtraction Test:")
    print(f"Subtracting {num2_sub} from {num1_sub}: {result_sub}") # Expected: 32

    num3_sub = 5
    num4_sub = 12
    result_sub_neg = subtract(num3_sub, num4_sub)
    print(f"Subtracting {num4_sub} from {num3_sub}: {result_sub_neg}") # Expected: -7

    print("\n--- Demo Complete ---")


# This ensures the 'run_cli_tests' function is only called when the script 
# is executed directly (e.g., in VS Code terminal using 'python calculator_app.py')
if __name__ == "__main__":
    run_cli_tests()