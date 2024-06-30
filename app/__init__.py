# app.py

# Import necessary modules
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
    """
    Handles commands and executes plugins.
    """
    def __init__(self, app):
        """
        Initializes the CommandHandler with an App instance.
        
        :param app: An instance of the App class.
        """
        self.app = app

    def handle_command(self, command, *args):
        """
        Handles a command by executing the corresponding plugin.
        
        :param command: The command to handle.
        :param args: The arguments for the command.
        """
        if command in self.app.commands:
            # Find the plugin corresponding to the command
            plugin = next(plugin for plugin in self.app.plugins if plugin.name == command)
            if plugin:
                # Execute the plugin
                return self.app.execute_plugin(plugin, *args)
            else:
                logging.warning(f"Plugin {command} not found")
                print(f"Plugin {command} not found")
        else:
            logging.warning(f"Unknown command: {command}")
            print(f"Unknown command: {command}. Type 'menu' to see available commands.")

class App:
    """
    The main application class.
    """
    def __init__(self, plugin_folder):
        """
        Initializes the App with a plugin folder.
        
        :param plugin_folder: The folder containing the plugins.
        """
        self.plugins = load_plugins(plugin_folder)
        # Create a dictionary of commands and their descriptions
        self.commands = {plugin.name: plugin.description for plugin in self.plugins}
        # Create a logs folder if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        # Configure logging
        self.configure_logging()
        # Load environment variables from a .env file
        load_dotenv()
        # Load environment variables
        self.settings = self.load_environment_variables()
        # Set a default environment if not set
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        # Create a CommandHandler instance
        self.command_handler = CommandHandler(self)
        # Create a history DataFrame
        self.history = pd.DataFrame(columns=['Command', 'Arguments', 'Result'])

    def configure_logging(self):
        """
        Configures logging.
        """
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            # Load logging configuration from a file
            logging.config.fileConfig(logging_conf_path)
        else:
            # Set up basic logging configuration
            logging.basicConfig(filename='app.log', level=logging.INFO)
            logging.info('Logging configured')
            logging.info('App started')

    def load_environment_variables(self):
        """
        Loads environment variables from the operating system and a .env file.
        
        :return: A dictionary of environment variables.
        """
        settings = {}
        # Load environment variables from the operating system
        settings['DEBUG'] = os.environ.get('DEBUG', False)
        settings['PLUGIN_DIR'] = os.environ.get('PLUGIN_DIR', 'plugins')
        # Load environment variables from the .env file
        load_dotenv()
        settings['ENVIRONMENT'] = os.environ.get('ENVIRONMENT', 'PRODUCTION')
        return settings

    def start(self):
        """
        Starts the application.
        """
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
        """
        Displays the calculation history.
        """
        print("\n Calculation History: \n")
        print(self.history)
        print("\n Available history commands: \n")
        for command, description in self.commands.items():
            if command in ["save_history", "load_history", "clear_history", "delete_history"]:
                print(f"{command.ljust(15)}: {description}")

    def execute_plugin(self, plugin, *args):
        """
        Executes a plugin.
        
        :param plugin: The plugin to execute.
        :param args: The arguments for the plugin.
        """
        # Get the logger for this module
        logger = logging.getLogger(__name__)
        try:
            # Check if the plugin is a mathematical operation
            if plugin.name in ["add", "subtract", "multiply", "divide"]:
                # Check if the plugin has exactly two arguments
                if len(args) != 2:
                    raise ValueError("Two arguments are required for this plugin")
                # Execute the plugin with the two arguments
                result = plugin.execute(float(args[0]), float(args[1]))
            else:
                # Execute the plugin with the history
                result = plugin.execute(self.history)
            # Log the successful execution of the plugin
            logger.info(f"Plugin {plugin.name} executed successfully with result {result}")
            # Append the result to the history
            self.history = self.history._append({'Command': plugin.name, 'Arguments': ', '.join(map(str, args)), 'Result': result}, ignore_index=True)
            # Print the result for certain plugins
            if plugin.name in ["add", "subtract", "multiply", "divide", "load_history"]:
                print(f"Result: {result}")
        except ValueError as e:
            # Log and print any ValueErrors that occur
            logger.error(f"Error executing plugin {plugin.name}: {e}")
            print(f"Error: {e}")


    def display_menu(self):
        # Get the logger for this module
        logger = logging.getLogger(__name__)
        # Log that the menu is being displayed
        logger.info("Displaying menu...")
        # Print the available commands
        print("Available commands: \n")
        # Iterate over the commands and print their descriptions
        for command, description in self.commands.items():
            if command in ["add", "subtract", "multiply", "divide"]:
                print(f"{command.ljust(10)}: {description}")
        # Print additional menu options
        print("\nType 'exit' to exit, 'menu' to display menu, or 'history' to display calculation history.")
