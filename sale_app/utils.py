from pathlib import Path
import json
from sale_app import app

def read_json(path):
    with open(path, 'r') as file:
        return json.load(file)
    
def load_categories():
    root_path = Path(app.root_path)
    path = root_path.joinpath('data', 'categories.json')
    return read_json(path)

def load_products():
    root_path = Path(app.root_path)
    path = root_path.joinpath('data', 'products.json')
    return read_json(path)
