from plugin import Plugin
import pandas as pd

class Save_historyPlugin(Plugin):
    def __init__(self):
        super().__init__("save_history", "Save calculation history to a file")

    def execute(self, history):
        # history = args[0]  # assume the first argument is the history dataframe
        history.to_csv('history.csv', index=False)
        # self.history.to_csv('history.csv', index=False)
        print("History saved to history.csv")