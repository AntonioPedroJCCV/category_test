import sys
sys.path.append(".")


from flask import Flask, render_template, request, redirect
from sqlalchemy.sql.expression import true, update

from back.controllers.category_controller import CategoryController
from back.models.category_model import Category

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/category')
def category():
    controller = CategoryController()
    category_list = controller.read_all()
    return render_template('category.html', category_list=category_list)

@app.route('/category/create', methods=['POST', 'GET'])
def create_category():
    if request.method == 'POST':
        controller = CategoryController()
        name = request.form.get('name')
        description = request.form.get('description')
        new_category = Category(name, description)
        controller.create(new_category)
        return redirect('/category')       
    return render_template('form_category.html', action = 'Create')

@app.route('/category/update/<int:id>', methods=['GET'])
def update_category_get(id):
    category = CategoryController().read_by_id(int(id))
    return render_template('form_category.html', category=category, action = 'Update')

@app.route('/category/update/', methods=['POST'])
def update_category_post():
    controller = CategoryController()
    id_ = request.form.get('id_')
    category = controller.read_by_id(int(id_))
    category.name = request.form.get('name')
    category.description = request.form.get('description')
    controller.update(category)
    return redirect('/category')      

@app.route('/category/delete/<int:id>')
def delete_category(id):
    category = CategoryController().read_by_id(id)
    CategoryController().delete(category)
    return redirect('/category')

app.run(debug=True)
