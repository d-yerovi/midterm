# clear_history_plugin.py
from plugin import Plugin
import pandas as pd

class Clear_historyPlugin(Plugin):
    """
    A plugin to clear the calculation history.
    """
    def __init__(self):
        """
        Initialize the plugin with its name and description.
        """
        super().__init__("clear_history", "Clear calculation history")

    def execute(self, history):
        """
        Clear the calculation history.
        
        :param history: The history dataframe to be cleared.
        """
        # Drop all rows from the history dataframe
        history.drop(history.index, inplace=True)
        print("History cleared")
