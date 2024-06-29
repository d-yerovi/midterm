# app.py
import importlib
import sys
import logging
import logging.config
from app.plugin_loader import load_plugins
import multiprocessing
import os
from dotenv import load_dotenv


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
            else:
                parts = user_input.split()
                command = parts[0]
                args = parts[1:]
                self.command_handler.handle_command(command, *args)
                '''
                for plugin in self.plugins:
                    if user_input.startswith(plugin.name):
                        _, num1, num2 = user_input.split()
                        p = multiprocessing.Process(target=self.execute_plugin, args=(plugin, float(num1), float(num2)))
                        p.start()
                        logger.info(f"Executing plugin {plugin.name} with arguments {num1} and {num2}")
                        break
                else:
                    logger.warning("Unknown command. Type 'menu' to see available commands.")
                    print("Unknown command. Type 'enu' to see available commands.")
                '''
    def execute_plugin(self, plugin, num1, num2):
        logger = logging.getLogger(__name__)
        try:
            result = plugin.execute(num1, num2)
            logger.info(f"Plugin {plugin.name} executed successfully with result {result}")
            print(f"Result: {result}")
        except ValueError as e:
            logger.error(f"Error executing plugin {plugin.name}: {e}")
            print(f"Error: {e}")

    def display_menu(self):
        logger = logging.getLogger(__name__)
        logger.info("Displaying menu...")
        print("Available commands:")
        for command, description in self.commands.items():
            print(f"{command}: {description}")