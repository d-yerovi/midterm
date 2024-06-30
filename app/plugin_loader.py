# plugin_loader.py
import os
import importlib.util

def load_plugins(plugin_folder):
    # Set the plugin folder path relative to the current file
    plugin_folder = os.path.join(os.path.dirname(__file__), 'plugins')
    # Initialize an empty list to store the loaded plugins
    plugins = []
    # Iterate over each file in the plugin folder
    for file in os.listdir(plugin_folder):
        # Check if the file is a Python module (i.e., it ends with ".py")
        if file.endswith(".py"):
            # Extract the module name from the file name (e.g., "my_plugin.py" -> "my_plugin")
            module_name = file[:-3]
            # Create a module specification from the file path
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(plugin_folder, file))
            # Create a module object from the specification
            module = importlib.util.module_from_spec(spec)
            # Execute the module (i.e., run its code)
            spec.loader.exec_module(module)
            # Get the plugin class from the module (assuming it's named "ModuleNamePlugin")
            plugin_class = getattr(module, module_name.capitalize() + "Plugin")
            # Create an instance of the plugin class and add it to the list
            plugins.append(plugin_class())
    # Return the list of loaded plugins
    return plugins
