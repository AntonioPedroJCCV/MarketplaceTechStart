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
    marketplace_lista = marketplaces()
    return render_template('marketplaces.html', marketplace_list = marketplace_lista)

@app.route('/categories')
def categoria():
    categorias_lista = categorias()
    return render_template('categories.html', categorias_lista = categorias_lista)

@app.route('/subcategories')
def subcategoria():
    subcategorias_lista = subcategorias()
    return render_template('subcategories.html', subcategorias_list = subcategorias_lista)

app.run(debug=True)