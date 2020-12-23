from flask import Flask, render_template
from marketplaces import marketplaces
from categories import categorias
from subcategories import subcategorias

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marketplaces')
def marketplace():
    marketplace_list = marketplaces()
    return render_template('marketplaces.html', list = marketplace_list)

@app.route('/categories')
def categoria():
    categorias_list = categorias()
    return render_template('categories.html', list = categorias_list)

@app.route('/subcategories')
def subcategoria():
    subcategorias_list = subcategorias()
    return render_template('subcategories.html', list = subcategorias_list)

app.run(debug=True)