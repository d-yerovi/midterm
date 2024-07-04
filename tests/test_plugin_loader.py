# tests/test_plugin_loader.py

import os
import importlib
from app.plugin_loader import load_plugins

def test_load_plugins():
    plugins = load_plugins('plugins')
    assert plugins
    for plugin in plugins:
        assert hasattr(plugin, 'name')
        assert hasattr(plugin, 'description')
        assert hasattr(plugin, 'execute')