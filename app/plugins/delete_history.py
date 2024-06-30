# delete_history_plugin.py
from plugin import Plugin
import os

class Delete_historyPlugin(Plugin):
    """
    A plugin to delete the calculation history file.
    """
    def __init__(self):
        """
        Initialize the plugin with its name and description.
        """
        super().__init__("delete_history", "Delete calculation history file")

    def execute(self, *args):
        """
        Execute the plugin's functionality: delete the history file if it exists.
        """
        if os.path.exists('history.csv'):
            # Remove the history file
            os.remove('history.csv')
            print("History file deleted")
        else:
            print("No history file found")
