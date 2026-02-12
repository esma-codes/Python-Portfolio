import os

def setup_project():
    """Initializes necessary folders for the project."""
    for folder in ["exchange_data", "logs"]:
        if not os.path.exists(folder):
            os.makedirs(folder)

