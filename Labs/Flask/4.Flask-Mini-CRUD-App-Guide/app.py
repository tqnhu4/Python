# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# --- Flask Configuration ---
# Secret key for sessions (required for flash messages)
app.secret_key = 'your_super_secret_key_for_crud_apps'

# SQLAlchemy Database Configuration for SQLite
# This will create a file named 'site.db' in your project directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Suppress warning
db = SQLAlchemy(app)

# --- Database Model for Products (for SQLite CRUD) ---
# This defines the structure of your 'Product' table in the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

# --- Create Database Tables (Run this once) ---
# It's good practice to create tables within an application context
# You can run this function manually or uncomment the line in if __name__ == '__main__':
def create_db():
    with app.app_context():
        db.create_all()
        print("Database tables created!")

# --- Global Data Storage (for In-memory To-Do and Notes) ---
# These lists will reset every time the server restarts
todo_items = [] # Stores strings for to-do tasks
notes = []      # Stores dictionaries for notes: [{'id': 1, 'title': 'My Note', 'content': '...'}]
next_note_id = 1 # To assign unique IDs to notes

# --- Main Index Route ---
@app.route('/')
def index():
    return render_template('index.html', page_title="Home")

# --- Level 4, Exercise 1: To-Do List (In-memory) ---

@app.route('/todo', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todo_items.append(task)
            flash('Task added successfully!', 'success')
        else:
            flash('Task cannot be empty!', 'error')
        return redirect(url_for('todo_list'))
    return render_template('todo.html', page_title="To-Do List", todos=todo_items)

@app.route('/todo/delete/<int:item_id>')
def delete_todo(item_id):
    if 0 <= item_id < len(todo_items):
        deleted_task = todo_items.pop(item_id)
        flash(f"Task '{deleted_task}' deleted successfully!", 'info')
    else:
        flash('Invalid task ID.', 'error')
    return redirect(url_for('todo_list'))

# --- Level 4, Exercise 2: Simple Notes App (In-memory CRUD) ---

@app.route('/notes')
def notes_list():
    return render_template('notes_list.html', page_title="My Notes", notes=notes)

@app.route('/notes/add', methods=['GET', 'POST'])
def add_note():
    global next_note_id
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            notes.append({'id': next_note_id, 'title': title, 'content': content})
            next_note_id += 1
            flash('Note added successfully!', 'success')
            return redirect(url_for('notes_list'))
        else:
            flash('Title and content cannot be empty!', 'error')
    return render_template('add_note.html', page_title="Add New Note")

@app.route('/notes/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note_to_edit = None
    for note in notes:
        if note['id'] == note_id:
            note_to_edit = note
            break
    
    if not note_to_edit:
        flash('Note not found!', 'error')
        return redirect(url_for('notes_list'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            note_to_edit['title'] = title
            note_to_edit['content'] = content
            flash('Note updated successfully!', 'success')
            return redirect(url_for('notes_list'))
        else:
            flash('Title and content cannot be empty!', 'error')
    
    return render_template('edit_note.html', page_title="Edit Note", note=note_to_edit)

@app.route('/notes/delete/<int:note_id>')
def delete_note(note_id):
    global notes
    original_len = len(notes)
    notes = [note for note in notes if note['id'] != note_id]
    if len(notes) < original_len:
        flash('Note deleted successfully!', 'info')
    else:
        flash('Note not found!', 'error')
    return redirect(url_for('notes_list'))

# --- Level 4, Exercise 3: Flask + SQLite (Actual CRUD) ---

@app.route('/products')
def products_list():
    products = Product.query.all() # Fetch all products from the database
    return render_template('products.html', page_title="Products", products=products)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price_str = request.form.get('price')
        description = request.form.get('description')

        if not name or not price_str:
            flash('Name and Price are required!', 'error')
            return render_template('add_product.html', page_title="Add Product")
        
        try:
            price = float(price_str)
        except ValueError:
            flash('Price must be a valid number!', 'error')
            return render_template('add_product.html', page_title="Add Product")

        new_product = Product(name=name, price=price, description=description)
        db.session.add(new_product)
        db.session.commit() # Save to database
        flash('Product added successfully!', 'success')
        return redirect(url_for('products_list'))
    
    return render_template('add_product.html', page_title="Add Product")

@app.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id) # Get product by ID, or return 404
    
    if request.method == 'POST':
        name = request.form.get('name')
        price_str = request.form.get('price')
        description = request.form.get('description')

        if not name or not price_str:
            flash('Name and Price are required!', 'error')
            return render_template('edit_product.html', page_title="Edit Product", product=product)
        
        try:
            price = float(price_str)
        except ValueError:
            flash('Price must be a valid number!', 'error')
            return render_template('edit_product.html', page_title="Edit Product", product=product)

        product.name = name
        product.price = price
        product.description = description
        db.session.commit() # Save changes to database
        flash('Product updated successfully!', 'success')
        return redirect(url_for('products_list'))
    
    return render_template('edit_product.html', page_title="Edit Product", product=product)

@app.route('/products/delete/<int:product_id>')
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit() # Delete from database
    flash('Product deleted successfully!', 'info')
    return redirect(url_for('products_list'))


# --- Run the Flask Application ---
if __name__ == '__main__':
    # IMPORTANT: Run create_db() ONCE to initialize your database.
    # You can comment it out after the first successful run.
    create_db() # This will create 'site.db' and the 'product' table.
    app.run(debug=True)