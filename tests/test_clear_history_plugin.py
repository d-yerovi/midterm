# test_clear_history_plugin.py
import pytest
from app.plugins.clear_history import Clear_historyPlugin
import pandas as pd

def test_clear_history_plugin_init():
    """
    Test that the plugin is initialized correctly.
    """
    plugin = Clear_historyPlugin()
    assert plugin.name == "clear_history"
    assert plugin.description == "Clear calculation history"

def test_clear_history_plugin_execute():
    """
    Test that the execute method clears the history dataframe.
    """
    plugin = Clear_historyPlugin()
    history = pd.DataFrame({"input": [1, 2, 3], "output": [2, 4, 6]})
    plugin.execute(history)
    assert history.empty
'''
def test_clear_history_plugin_execute_prints_message(capsys):
    """
    Test that the execute method prints a message when clearing the history.
    """
    plugin = Clear_historyPlugin()
    history = pd.DataFrame({"input": [1, 2, 3], "output": [2, 4, 6]})
    plugin.execute(history)
    captured = capsys.readouterr()
    assert captured.out.strip() == "History cleared\n"
'''