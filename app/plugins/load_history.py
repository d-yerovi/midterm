from plugin import Plugin
import pandas as pd

class Load_historyPlugin(Plugin):
    def __init__(self):
        super().__init__("load_history", "Load calculation history from a file")

    def execute(self, *args):
        try:
            history = pd.read_csv('history.csv')
            print("History loaded from history.csv")
            return history
        except FileNotFoundError:
            print("No history file found")
            return None