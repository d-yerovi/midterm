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
        self.name = "delete_history"
        self.description = "Delete calculation history file"

    def execute(self, *args):
        """
        Execute the plugin's functionality: delete the history file if it exists.
        """
        history_file = "history.csv"
        if os.path.exists(history_file):
            try:
                os.remove(history_file)
                print("History file deleted")
            except OSError as e:
                print(f"Error deleting history file: {e}")
        else:
            print("No history file found")
