# tests/test_save_history_plugin.py

import pytest
from app import App
from app.plugins.save_history import Save_historyPlugin
import pandas as pd
import os

@pytest.fixture
def app():
    # Create an instance of the App class
    return App("plugins")

@pytest.fixture
def save_history_plugin():
    # Create an instance of the Save_historyPlugin class
    return Save_historyPlugin()

def test_save_history_plugin_execute(app, save_history_plugin):
    # Create a sample history DataFrame
    history = pd.DataFrame({'Command': ['add', 'subtract'], 'Arguments': ['1, 2', '3, 4'], 'Result': [3, -1]})
    app.history = history
    
    # Execute the Save_historyPlugin
    save_history_plugin.execute(app.history)
    
    # Check that the history was saved to a CSV file
    assert os.path.exists('history.csv')
    
    # Load the saved CSV file and compare it with the original history
    saved_history = pd.read_csv('history.csv')
    pd.testing.assert_frame_equal(history, saved_history)
    
    # Clean up by deleting the saved CSV file
    os.remove('history.csv')

def test_save_history_plugin_execute_empty_history(app, save_history_plugin):
    # Create an empty history DataFrame
    app.history = pd.DataFrame(columns=['Command', 'Arguments', 'Result'])
    
    # Execute the Save_historyPlugin
    save_history_plugin.execute(app.history)
    
    # Check that the history was saved to a CSV file
    assert os.path.exists('history.csv')
    
    # Load the saved CSV file and compare it with the original history
    saved_history = pd.read_csv('history.csv')
    pd.testing.assert_frame_equal(app.history, saved_history)
    
    # Clean up by deleting the saved CSV file
    os.remove('history.csv')