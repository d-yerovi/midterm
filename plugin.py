# plugin.py
class Plugin:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def execute(self, *args, **kwargs):
        raise NotImplementedError("Plugin must implement execute method")