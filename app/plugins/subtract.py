# plugins/subtract.py
# Import the Plugin class from the plugin module
from plugin import Plugin
# Import the subtract function from the calculator.operations module
from calculator.operations import subtract

# Define a SubtractPlugin class that inherits from Plugin
class SubtractPlugin(Plugin):
    # Initialize the SubtractPlugin with a name and description
    def __init__(self):
        # Call the constructor of the Plugin class with the name "subtract" and description "Subtract two numbers"
        super().__init__("subtract", "Subtract two numbers")

    # Define an execute method that takes two numbers as input and returns their difference
    def execute(self, num1, num2):
        # Convert the input numbers to floats and subtract them using the subtract function
        return subtract(float(num1), float(num2))
