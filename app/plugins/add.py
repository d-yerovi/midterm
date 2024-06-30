# plugins/add.py
# Import the Plugin class from the plugin module
from plugin import Plugin
# Import the add function from the calculator.operations module
from calculator.operations import add

# Define a class AddPlugin that inherits from Plugin
class AddPlugin(Plugin):
    # Initialize the AddPlugin instance
    def __init__(self):
        # Call the constructor of the parent class (Plugin) with the name "add" and description "Add two numbers"
        super().__init__("add", "Add two numbers")

    # Define a method to execute the add operation
    def execute(self, num1, num2):
        # Convert the input numbers to floats and return their sum using the add function
        return add(float(num1), float(num2))
