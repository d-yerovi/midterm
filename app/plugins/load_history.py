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
        self.name = "load_history"
        self.description = "Load calculation history from a file"

    def execute(self, file_path=None):
        """
        Load the calculation history from a file.
        
        :return: The loaded history dataframe or None if no file is found.
        """
        if file_path is None:
            file_path = "history.csv"  # assume this is the default file name
        try:
            # Read the history from a CSV file
            file_path = "history.csv"
            history = pd.read_csv(file_path)
            return history
        except FileNotFoundError:
            # Handle the case where the file is not found
            print("No history file found")
            return None
        except pd.errors.ParserError as e:
            # Re-raise the ParserError exception
            print("Error parsing history file")
            raise