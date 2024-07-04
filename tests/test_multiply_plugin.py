# tests/test_multyply_plugin.py
import pytest
from app.plugins.multiply import MultiplyPlugin

def test_multiply_plugin_init():
    plugin = MultiplyPlugin()
    assert plugin.name == "multiply"
    assert plugin.description == "Multiply two numbers"

def test_multiply_plugin_execute():
    plugin = MultiplyPlugin()
    result = plugin.execute("2", "3")
    assert result == 6.0

def test_multiply_plugin_execute_negative_numbers():
    plugin = MultiplyPlugin()
    result = plugin.execute("-2", "3")
    assert result == -6.0

def test_multiply_plugin_execute_non_numeric_input():
    plugin = MultiplyPlugin()
    with pytest.raises(ValueError):
        plugin.execute("two", "3")

def test_multiply_plugin_execute_invalid_input():
    plugin = MultiplyPlugin()
    with pytest.raises(TypeError):
        plugin.execute("2", None)