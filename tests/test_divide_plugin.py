# tests/test_multyply_plugin.py
import pytest
from app.plugins.divide import DividePlugin

def test_divide_plugin_init():
    plugin = DividePlugin()
    assert plugin.name == "divide"
    assert plugin.description == "Divide two numbers"

def test_divide_plugin_execute():
    plugin = DividePlugin()
    result = plugin.execute("9", "3")
    assert result == 3.0

def test_divide_plugin_execute_negative_numbers():
    plugin = DividePlugin()
    result = plugin.execute("-9", "3")
    assert result == -3.0

def test_divide_plugin_execute_non_numeric_input():
    plugin = DividePlugin()
    with pytest.raises(ValueError):
        plugin.execute("two", "3")

def test_divide_plugin_execute_invalid_input():
    plugin = DividePlugin()
    with pytest.raises(TypeError):
        plugin.execute("2", None)