# main.py
from app import App   
import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

# Define the main function
def main():
    # Check if the command line arguments are valid
    if len(sys.argv) != 4:
        # If not, print the usage message and exit with an error code
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    # Extract the command line arguments
    _, a, b, operation = sys.argv
    # Call the calculate_and_print function with the extracted arguments
    calculate_and_print(a, b, operation)

# If this script is run directly (not imported as a module), execute the main function
if __name__ == "__main__":
    # Create an App instance with the 'plugins' argument
    app = App('plugins')
    # Start the App instance
    app.start()