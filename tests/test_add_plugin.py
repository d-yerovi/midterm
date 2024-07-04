# tests/test_add_plugin.py
import pytest
from app.plugins.add import AddPlugin

def test_add_plugin_init():
    plugin = AddPlugin()
    assert plugin.name == "add"
    assert plugin.description == "Add two numbers"

def test_add_plugin_execute():
    plugin = AddPlugin()
    result = plugin.execute("2", "3")
    assert result == 5.0

def test_add_plugin_execute_negative_numbers():
    plugin = AddPlugin()
    result = plugin.execute("-2", "3")
    assert result == 1.0

def test_add_plugin_execute_non_numeric_input():
    plugin = AddPlugin()
    with pytest.raises(ValueError):
        plugin.execute("two", "3")

def test_add_plugin_execute_invalid_input():
    plugin = AddPlugin()
    with pytest.raises(TypeError):
        plugin.execute("2", None)