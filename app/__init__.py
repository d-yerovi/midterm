# app.py
import importlib
import sys
import logging
import logging.config
from app.plugin_loader import load_plugins
import multiprocessing
import os
from dotenv import load_dotenv
import pandas as pd

class CommandHandler:
    def __init__(self, app):
        self.app = app

    def handle_command(self, command, *args):
        if command in self.app.commands:
            plugin = next(plugin for plugin in self.app.plugins if plugin.name == command)
            if plugin:
                return self.app.execute_plugin(plugin, *args)
            else:
                logging.warning(f"Plugin {command} not found")
                print(f"Plugin {command} not found")
        else:
            logging.warning(f"Unknown command: {command}")
            print(f"Unknown command: {command}. Type 'menu' to see available commands.")

class App:
    def __init__(self, plugin_folder):
        self.plugins = load_plugins(plugin_folder)
        self.commands = {plugin.name: plugin.description for plugin in self.plugins}
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler(self)
        self.history = pd.DataFrame(columns=['Command', 'Arguments', 'Result'])

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path)
        else:
            logging.basicConfig(filename='app.log', level=logging.INFO)
            logging.info('Logging configured')
            logging.info('App started')

    def load_environment_variables(self):
        settings = {}
        # Load environment variables from the operating system
        settings['DEBUG'] = os.environ.get('DEBUG', False)
        settings['PLUGIN_DIR'] = os.environ.get('PLUGIN_DIR', 'plugins')
        # Load environment variables from the .env file
        load_dotenv()
        settings['ENVIRONMENT'] = os.environ.get('ENVIRONMENT', 'PRODUCTION')
        return settings

    def start(self):
        logger = logging.getLogger(__name__)
        logger.info("Starting application...")
        print("Hello World. Type 'exit' to exit.")
        self.display_menu()
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                logger.info("Exiting...")
                print("Exiting...")
                break
            elif user_input.lower() == "menu":
                self.display_menu()
            elif user_input.lower() == "history":
                self.display_history()
            else:
                parts = user_input.split()
                command = parts[0]
                args = parts[1:]
                self.command_handler.handle_command(command, *args)

    def display_history(self):
        print("Calculation History:")
        print(self.history)
        print("Available history commands: \n")
        for command, description in self.commands.items():
            if command in ["save_history", "load_history", "clear_history", "delete_history"]:
                print(f"{command.ljust(15)}: {description}")

    def execute_plugin(self, plugin, *args):
        logger = logging.getLogger(__name__)
        try:
            if plugin.name in ["add", "subtract", "multiply", "divide"]:
                if len(args) != 2:
                    raise ValueError("Two arguments are required for this plugin")
                result = plugin.execute(float(args[0]), float(args[1]))
            else:
                result = plugin.execute(self.history)
            logger.info(f"Plugin {plugin.name} executed successfully with result {result}")
            self.history = self.history._append({'Command': plugin.name, 'Arguments': ', '.join(map(str, args)), 'Result': result}, ignore_index=True)
            if plugin.name in ["add", "subtract", "multiply", "divide", "load_history"]: print(f"Result: {result}")
        except ValueError as e:
            logger.error(f"Error executing plugin {plugin.name}: {e}")
            print(f"Error: {e}")

    def display_menu(self):
        logger = logging.getLogger(__name__)
        logger.info("Displaying menu...")
        print("Available commands: \n")
        for command, description in self.commands.items():
            if command in ["add", "subtract", "multiply", "divide"]:
                print(f"{command.ljust(10)}: {description}")
        print("\nType 'exit' to exit, 'menu' to display menu, or 'history' to display calculation history.")
