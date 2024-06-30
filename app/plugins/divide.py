# plugins/divide.py
# Import the Plugin class from the plugin module
from plugin import Plugin
# Import the divide function from the calculator.operations module
from calculator.operations import divide

# Define a class DividePlugin that inherits from Plugin
class DividePlugin(Plugin):
    # Initialize the DividePlugin with a name and description
    def __init__(self):
        # Call the constructor of the parent class (Plugin) with the name "divide" and description "Divide two numbers"
        super().__init__("divide", "Divide two numbers")

    # Define a method execute that takes two numbers as input and returns their division
    def execute(self, num1, num2):
        # Check if the second number is zero to avoid division by zero error
        if num2 == 0:
            # Raise a ValueError with a message if the second number is zero
            raise ValueError("Division by zero is not allowed")
        # Return the result of dividing the first number by the second number
        return divide(float(num1), float(num2))
