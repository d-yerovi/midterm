'''test app functionality and menu option'''

# import pytest
from app import App
def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App('plugins')  # Create an instance of the App class
    app.start()  # Call the start method on the instance
    out, err = capfd.readouterr()
    if err:
        print("Error:", err)

    # Check that the initial greeting is printed and the REPL exits gracefully
    assert "Hello World. Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App('plugins')  # Create an instance of the App class
    app.start()  # Call the start method on the instance
    out, err = capfd.readouterr()
    if err:
        print("Error:", err)
    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    assert "Hello World. Type 'exit' to exit." in out
    assert "Available commands:" in out
    assert "Unknown command: unknown_command. Type 'menu' to see available commands." in out
