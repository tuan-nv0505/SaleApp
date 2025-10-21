from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from flask import render_template
from sale_app import app
import utils

@app.route('/')
def home():
    return render_template(
        'index.html',
        categories=utils.load_categories()
    )

@app.route('/products')
def product_list():
    return render_template(
        'products.html',
        products=utils.load_products()
    )

if __name__ == '__main__':
    app.run(debug=True)