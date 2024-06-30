from plugin import Plugin
import os

class Delete_historyPlugin(Plugin):
    def __init__(self):
        super().__init__("delete_history", "Delete calculation history file")

    def execute(self, *args):
        if os.path.exists('history.csv'):
            os.remove('history.csv')
            print("History file deleted")
        else:
            print("No history file found")