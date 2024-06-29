# plugins/multiply.py
from plugin import Plugin
from calculator.operations import multiply

class MultiplyPlugin(Plugin):
    def __init__(self):
        super().__init__("multiply", "Multiply two numbers")

    def execute(self, num1, num2):
        return multiply(float(num1), float(num2))