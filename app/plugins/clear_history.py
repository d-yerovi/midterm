from plugin import Plugin
import pandas as pd

class Clear_historyPlugin(Plugin):
    def __init__(self):
        super().__init__("clear_history", "Clear calculation history")

    def execute(self, history):
        # self.clear_history()
        # self.history = pd.DataFrame(columns=['Command', 'Arguments', 'Result'])
        # history = [0]  # assume the first argument is the history dataframe
        history.drop(history.index, inplace=True)
        print("History cleared")