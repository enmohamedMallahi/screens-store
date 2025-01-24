from flask import Flask, render_template
import json

app = Flask(__name__)

# Load products from JSON file
def load_products():
    with open('data/products.json', 'r') as f:
        return json.load(f)

products = load_products()

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<product_id>')
def product(product_id):
    product_data = products.get(product_id)
    if product_data:
        return render_template('product.html', product=product_data)
    return 'Product not found', 404

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products_page():
    # Group products by category
    categorized_products = {}
    for product in products.values():
        category = product.get('category', 'other')
        if category not in categorized_products:
            categorized_products[category] = []
        categorized_products[category].append(product)
    return render_template('products.html', categories=categorized_products)

if __name__ == '__main__':
    app.run(debug=True) 