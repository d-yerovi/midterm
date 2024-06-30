# load_history_plugin.py
from plugin import Plugin
import pandas as pd

class Load_historyPlugin(Plugin):
    """
    A plugin to load the calculation history from a file.
    """
    def __init__(self):
        """
        Initialize the plugin with its name and description.
        """
        super().__init__("load_history", "Load calculation history from a file")

    def execute(self, *args):
        """
        Load the calculation history from a file.
        
        :return: The loaded history dataframe or None if no file is found.
        """
        try:
            # Read the history from a CSV file
            history = pd.read_csv('history.csv')
            print("History loaded from history.csv")
            return history
        except FileNotFoundError:
            # Handle the case where the file is not found
            print("No history file found")
            return None
