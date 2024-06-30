# plugins/multiply.py
# Import the Plugin class from the plugin module
from plugin import Plugin
# Import the multiply function from the calculator.operations module
from calculator.operations import multiply

# Define a class MultiplyPlugin that inherits from Plugin
class MultiplyPlugin(Plugin):
    # Initialize the MultiplyPlugin with a name and description
    def __init__(self):
        # Call the constructor of the parent class (Plugin) with the name "multiply" and description "Multiply two numbers"
        super().__init__("multiply", "Multiply two numbers")

    # Define a method execute that takes two numbers as input and returns their product
    def execute(self, num1, num2):
        # Convert the input numbers to floats and pass them to the multiply function
        return multiply(float(num1), float(num2))
