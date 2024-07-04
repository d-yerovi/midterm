# tests/test_subtract_plugin.py
import pytest
from app.plugins.subtract import SubtractPlugin

def test_subtract_plugin_init():
    plugin = SubtractPlugin()
    assert plugin.name == "subtract"
    assert plugin.description == "Subtract two numbers"

def test_subtract_plugin_execute():
    plugin = SubtractPlugin()
    result = plugin.execute("2", "3")
    assert result == -1.0

def test_subtract_plugin_execute_negative_numbers():
    plugin = SubtractPlugin()
    result = plugin.execute("-2", "3")
    assert result == -5.0

def test_subtract_plugin_execute_non_numeric_input():
    plugin = SubtractPlugin()
    with pytest.raises(ValueError):
        plugin.execute("two", "3")

def test_subtract_plugin_execute_invalid_input():
    plugin = SubtractPlugin()
    with pytest.raises(TypeError):
        plugin.execute("2", None)