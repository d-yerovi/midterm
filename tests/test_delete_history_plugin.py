# test_delete_history_plugin.py
import os
import pytest
from app.plugins.delete_history import Delete_historyPlugin

@pytest.fixture
def delete_history_plugin():
    return Delete_historyPlugin()

def test_init(delete_history_plugin):
    assert delete_history_plugin.name == "delete_history"
    assert delete_history_plugin.description == "Delete calculation history file"

def test_execute_file_exists(delete_history_plugin, tmp_path):
    # Create a temporary history file
    history_file = tmp_path / "history.csv"
    history_file.touch()

    # Execute the plugin
    delete_history_plugin.execute(str(history_file))

    # Assert the file is deleted
    assert history_file.exists()
    assert "History file deleted"

def test_execute_file_does_not_exist(delete_history_plugin, capfd):
    # Execute the plugin
    delete_history_plugin.execute()

    # Assert the correct message is printed
    assert "No history file found" in capfd.readouterr().out

def test_execute_file_exists_but_cannot_be_deleted(delete_history_plugin, tmp_path, monkeypatch, capfd):
    # Create a temporary history file
    history_file = tmp_path / "history.csv"
    history_file.touch()

    # Mock os.remove to raise an OSError
    def mock_remove(path):
        raise OSError("Permission denied")

    monkeypatch.setattr(os, "remove", mock_remove)

    # Execute the plugin
    delete_history_plugin.execute(str(history_file))

    # Assert the file still exists
    assert history_file.exists()
    assert "Error deleting history file: Permission denied"