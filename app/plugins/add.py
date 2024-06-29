# plugins/add.py
from plugin import Plugin
from calculator.operations import add

class AddPlugin(Plugin):
    def __init__(self):
        super().__init__("add", "Add two numbers")

    def execute(self, num1, num2):
        return add(float(num1),float(num2))