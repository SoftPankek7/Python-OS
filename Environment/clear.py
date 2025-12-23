''' Simple Clear Screen Utility (Built-in)'''

class Environment:
    LibInfo = {
        "name": "Clear",
        "credits": [],
        "version": 1.0,
        "reqVersion": 1.3,
        "description": "Simple Clear Screen Utility (Built-in)",
        "helpinfo": "Just type clear to empty the screen."
    }
    def RunFromEnv(func):
        import os
        os.system("cls" if os.name == "nt" else "clear")