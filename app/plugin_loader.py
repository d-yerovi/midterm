# plugin_loader.py
import os
import importlib.util

def load_plugins(plugin_folder):
    plugin_folder = os.path.join(os.path.dirname(__file__), 'plugins')
    plugins = []
    for file in os.listdir(plugin_folder):
        if file.endswith(".py"):
            module_name = file[:-3]
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(plugin_folder, file))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            plugin_class = getattr(module, module_name.capitalize() + "Plugin")
            plugins.append(plugin_class())
    return plugins