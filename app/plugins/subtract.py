# plugins/subtract.py
from plugin import Plugin
from calculator.operations import subtract

class SubtractPlugin(Plugin):
    def __init__(self):
        super().__init__("subtract", "Subtract two numbers")

    def execute(self, num1, num2):
        return subtract(float(num1),float(num2))