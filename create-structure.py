import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)
    print(f"Created file: {path}")

# Project structure
project_structure = {
    "src": {
        "assets": {
            "images": {},
            "audio": {}
        },
        "js": {
            "scenes": {
                "BootScene.js": "",
                "LoadingScene.js": "",
                "MainMenuScene.js": "",
                "GameScene.js": ""
            },
            "entities": {
                "Pacman.js": "",
                "Ghost.js": "",
                "Pellet.js": ""
            },
            "config.js": "",
            "game.js": ""
        },
        "index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Pacman Clone</title>\n</head>\n<body>\n    <script src=\"https://cdn.jsdelivr.net/npm/phaser@3.55.2/dist/phaser.min.js\"></script>\n    <script src=\"js/config.js\"></script>\n    <script src=\"js/game.js\"></script>\n</body>\n</html>"
    }
}

def create_project_structure(base_path, structure):
    for item, sub_items in structure.items():
        path = os.path.join(base_path, item)
        if isinstance(sub_items, dict):
            create_directory(path)
            create_project_structure(path, sub_items)
        else:
            create_file(path, sub_items)

# Create the project structure
create_project_structure("pacman_clone", project_structure)

print("Pacman clone project structure created successfully!")
