# test_load_history_plugin.py
import pytest
from app.plugins.load_history import Load_historyPlugin
import pandas as pd
import os

def test_load_history_plugin_init():
    """
    Test that the Load_historyPlugin is initialized correctly.
    """
    plugin = Load_historyPlugin()
    assert plugin.name == "load_history"
    assert plugin.description == "Load calculation history from a file"

def test_load_history_plugin_execute_found_file():
    """
    Test that the Load_historyPlugin can load a history file.
    """
    # Create a temporary history file
    file_path = "history.csv"
    data = {"Command": ["add", "subtract"], "Arguments": ["1, 2", "3, 4"], "Result": [3, -1]}
    pd.DataFrame(data).to_csv(file_path, index=False)
    
    plugin = Load_historyPlugin()
    history = plugin.execute(file_path)
    
    # Check that the history was loaded correctly
    assert isinstance(history, pd.DataFrame)
    assert history.shape == (2, 3)
    assert history.columns.tolist() == ["Command", "Arguments", "Result"]
    
    # Clean up the temporary file
    os.remove(file_path)

def test_load_history_plugin_execute_not_found_file():
    """
    Test that the Load_historyPlugin handles a missing history file.
    """
    plugin = Load_historyPlugin()
    history = plugin.execute("non_existent_file.csv")
    assert history is None
'''
def test_load_history_plugin_execute_invalid_file(capsys):
    """
    Test that the Load_historyPlugin handles an invalid history file.
    """
    # Create a temporary invalid history file
    file_path = "history.csv"
    with open(file_path, "w") as f:
        f.write("Invalid CSV file")
    
    plugin = Load_historyPlugin()
    plugin.execute(file_path)
    
    # Check that the error message is printed
    captured = capsys.readouterr()
    assert "Error parsing history file" in captured.out
    
    # Clean up the temporary file
    os.remove(file_path)
'''