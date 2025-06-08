import json
from pathlib import Path
import shutil

def init_project():
    """
    Initialize the project.
    """
    folder_path = Path("functions")
    folder_path.mkdir(parents=True, exist_ok=True)

    current_file = Path(__file__).resolve()
    template_path = current_file.parent / "templates"
    files_to_copy = ["__init__.py", "example.py"]

    for file_name in files_to_copy:
        src = template_path / file_name
        dst = folder_path / file_name
        if not dst.exists():
            shutil.copy(src, dst)
        else:
            pass
    
    func_json_path = folder_path / "func.json"
    if not func_json_path.exists():
        func_json = {
            "functions": [
                {
                    "name": "greet",
                    "description": "Greet a person",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "Name of the person to greet"
                            }
                        },
                        "required": ["name"]
                    }
                }
            ]
        }

        with open(func_json_path, 'w') as f:
            json.dump(func_json, f, indent=4)
