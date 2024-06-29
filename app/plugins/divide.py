# plugins/divide.py
from plugin import Plugin
from calculator.operations import divide

class DividePlugin(Plugin):
    def __init__(self):
        super().__init__("divide", "Divide two numbers")

    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return divide(float(num1), float(num2))