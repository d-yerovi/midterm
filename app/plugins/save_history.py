from plugin import Plugin
import pandas as pd

# Define a new Plugin class called Save_historyPlugin
class Save_historyPlugin(Plugin):
    # Initialize the class with a unique name and a description
    def __init__(self):
        super().__init__("save_history", "Save calculation history to a file")

    # Define a method called execute that takes a single argument: history
    def execute(self, history):
        # history = args[0]  # You can comment out this line since you're using the history argument directly
        # Save the history DataFrame to a CSV file called 'history.csv'
        # index=False ensures that the DataFrame index is not saved as a column in the CSV file
        history.to_csv('history.csv', index=False)
        # Print a message to the console to confirm that the history was saved
        print("History saved to history.csv")
