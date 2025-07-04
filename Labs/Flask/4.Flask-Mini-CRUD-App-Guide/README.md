# Flask Mini CRUD App Guide (Level 4)

This guide will walk you through building three different mini-CRUD (Create, Read, Update, Delete) applications using Flask. You'll start with in-memory data storage (lists) and then move to persistent storage using SQLite.

-----

### 1\. Project Setup and Initial Installation

Let's get your development environment ready for all three mini-apps.

1.  **Install Flask and Flask-SQLAlchemy:**
    Open your terminal or command prompt. You'll need Flask for all parts and `Flask-SQLAlchemy` specifically for the SQLite database part.

    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

2.  **Create Your Project Folder:**
    Make a new directory for this Flask application. Let's call it `flask_crud_apps`.

    ```bash
    mkdir flask_crud_apps
    cd flask_crud_apps
    ```

3.  **Create `app.py`:**
    Inside `flask_crud_apps`, create a Python file named `app.py`. This file will contain all your Flask application's backend code.

4.  **Create `templates` Folder:**
    Flask needs a dedicated folder for your HTML template files. Create a new folder named `templates` inside `flask_crud_apps`.

    ```bash
    mkdir templates
    ```

5.  **Create HTML Files:**
    Inside the `templates` folder, create the following empty HTML files. We'll fill them with content for each exercise.

      * `base.html` (for common layout)
      * `index.html` (main menu)
      * `todo.html`
      * `notes_list.html`
      * `add_note.html`
      * `edit_note.html`
      * `products.html`
      * `add_product.html`
      * `edit_product.html`

-----

### 2\. Base Template (`templates/base.html`)

This `base.html` file will provide a consistent layout for all your pages, demonstrating template inheritance. Copy and paste this into `templates/base.html`.

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %} - Flask CRUD Apps</title>
    <!-- Tailwind CSS CDN for quick styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex flex-col">
    <nav class="bg-blue-700 p-4 text-white shadow-md">
        <div class="container mx-auto flex justify-between items-center">
            <a href="/" class="text-2xl font-bold hover:text-blue-200 transition duration-300">Flask Mini CRUD Apps</a>
            <ul class="flex space-x-6">
                <li><a href="/todo" class="hover:text-blue-200 transition duration-300">To-Do List</a></li>
                <li><a href="/notes" class="hover:text-blue-200 transition duration-300">Notes App</a></li>
                <li><a href="/products" class="hover:text-blue-200 transition duration-300">Products (SQLite)</a></li>
            </ul>
        </div>
    </nav>

    <div class="container mx-auto p-6 flex-grow">
        <!-- Flash messages display here -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <ul class="mb-4">
                {% for category, message in messages %}
                    <li class="p-3 rounded-md mb-2 
                                {% if category == 'success' %} bg-green-200 text-green-800
                                {% elif category == 'error' %} bg-red-200 text-red-800
                                {% elif category == 'info' %} bg-blue-200 text-blue-800
                                {% elif category == 'warning' %} bg-yellow-200 text-yellow-800
                                {% endif %}">
                        {{ message }}
                    </li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <footer class="bg-gray-800 text-white p-4 text-center mt-auto">
        <p>&copy; 2025 Flask Mini CRUD Apps. All rights reserved.</p>
    </footer>
</body>
</html>
```

-----

### 3\. Main Application File (`app.py`)

This `app.py` file will contain all the Flask routes and logic for your three mini-apps. It's structured with comments to clearly separate each section.

```python
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
```

-----

### 4\. HTML Template Files (`templates` folder)

These HTML files are designed to work with the `app.py` and inherit from `base.html`.

#### `templates/index.html` (Main Menu)

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-blue-800 mb-6">Welcome to Flask Mini CRUD Apps!</h1>
        <p class="text-lg text-gray-700 mb-8">Choose an application to explore:</p>
        <ul class="space-y-4">
            <li><a href="/todo" class="block bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">To-Do List (In-memory)</a></li>
            <li><a href="/notes" class="block bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">Simple Notes App (In-memory)</a></li>
            <li><a href="/products" class="block bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">Products (Flask + SQLite)</a></li>
        </ul>
    </div>
</div>
{% endblock %}
```

#### `templates/todo.html` (To-Do List)

```html
<!-- templates/todo.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex flex-col items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-lg w-full text-center">
        <h1 class="text-3xl font-bold text-blue-600 mb-6">{{ page_title }}</h1>
        
        <form method="POST" action="{{ url_for('todo_list') }}" class="flex mb-6 space-x-2">
            <input type="text" name="task" placeholder="Add a new task..." 
                   class="flex-grow p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required>
            <button type="submit" 
                    class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Add Task
            </button>
        </form>

        <ul class="space-y-3 text-left">
            {% if todos %}
                {% for todo in todos %}
                    <li class="flex items-center justify-between bg-gray-50 p-3 rounded-md shadow-sm">
                        <span class="text-lg text-gray-800">{{ loop.index }}. {{ todo }}</span>
                        <a href="{{ url_for('delete_todo', item_id=loop.index0) }}" 
                           class="bg-red-500 hover:bg-red-600 text-white text-sm px-3 py-1 rounded-md transition duration-300">
                            Delete
                        </a>
                    </li>
                {% endfor %}
            {% else %}
                <li class="text-center text-gray-500">No tasks yet! Add some above.</li>
            {% endif %}
        </ul>
        <a href="/" class="text-blue-500 hover:underline mt-6 block">Back to Home</a>
    </div>
</div>
{% endblock %}
```

#### `templates/notes_list.html` (Notes List)

```html
<!-- templates/notes_list.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex flex-col items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-2xl w-full text-center">
        <h1 class="text-3xl font-bold text-green-600 mb-6">{{ page_title }}</h1>
        
        <a href="{{ url_for('add_note') }}" 
           class="inline-block bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-md mb-6 transition duration-300">
            Add New Note
        </a>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-left">
            {% if notes %}
                {% for note in notes %}
                    <div class="bg-gray-50 p-4 rounded-md shadow-sm border border-gray-200">
                        <h2 class="text-xl font-semibold text-gray-900 mb-2">{{ note.title }}</h2>
                        <p class="text-gray-700 text-sm mb-4 line-clamp-3">{{ note.content }}</p>
                        <div class="flex justify-end space-x-2">
                            <a href="{{ url_for('edit_note', note_id=note.id) }}" 
                               class="bg-yellow-500 hover:bg-yellow-600 text-white text-sm px-3 py-1 rounded-md transition duration-300">
                                Edit
                            </a>
                            <a href="{{ url_for('delete_note', note_id=note.id) }}" 
                               class="bg-red-500 hover:bg-red-600 text-white text-sm px-3 py-1 rounded-md transition duration-300"
                               onclick="return confirm('Are you sure you want to delete this note?');">
                                Delete
                            </a>
                        </div>
                    </div>
                {% endfor %}
            {% else %}
                <p class="text-center text-gray-500 col-span-full">No notes yet! Click "Add New Note" to create one.</p>
            {% endif %}
        </div>
        <a href="/" class="text-green-500 hover:underline mt-6 block">Back to Home</a>
    </div>
</div>
{% endblock %}
```

#### `templates/add_note.html` (Add Note Form)

```html
<!-- templates/add_note.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-green-600 mb-6">{{ page_title }}</h1>
        
        <form method="POST" action="{{ url_for('add_note') }}" class="space-y-4">
            <input type="text" name="title" placeholder="Note Title" 
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500" required>
            <textarea name="content" placeholder="Note Content" rows="6"
                      class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500" required></textarea>
            <button type="submit" 
                    class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Save Note
            </button>
        </form>
        <a href="{{ url_for('notes_list') }}" class="text-green-500 hover:underline mt-4 block">Back to Notes List</a>
    </div>
</div>
{% endblock %}
```

#### `templates/edit_note.html` (Edit Note Form)

```html
<!-- templates/edit_note.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-yellow-600 mb-6">{{ page_title }}</h1>
        
        <form method="POST" action="{{ url_for('edit_note', note_id=note.id) }}" class="space-y-4">
            <input type="text" name="title" placeholder="Note Title" value="{{ note.title }}"
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500" required>
            <textarea name="content" placeholder="Note Content" rows="6"
                      class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500" required>{{ note.content }}</textarea>
            <button type="submit" 
                    class="w-full bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Update Note
            </button>
        </form>
        <a href="{{ url_for('notes_list') }}" class="text-yellow-500 hover:underline mt-4 block">Back to Notes List</a>
    </div>
</div>
{% endblock %}
```

#### `templates/products.html` (Products List - SQLite)

```html
<!-- templates/products.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex flex-col items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-3xl w-full text-center">
        <h1 class="text-3xl font-bold text-purple-600 mb-6">{{ page_title }} (SQLite Database)</h1>
        
        <a href="{{ url_for('add_product') }}" 
           class="inline-block bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-md mb-6 transition duration-300">
            Add New Product
        </a>

        <div class="overflow-x-auto">
            <table class="min-w-full bg-white border border-gray-200 rounded-lg shadow-sm">
                <thead>
                    <tr class="bg-gray-100 text-gray-600 uppercase text-sm leading-normal">
                        <th class="py-3 px-6 text-left">ID</th>
                        <th class="py-3 px-6 text-left">Name</th>
                        <th class="py-3 px-6 text-left">Price</th>
                        <th class="py-3 px-6 text-left">Description</th>
                        <th class="py-3 px-6 text-center">Actions</th>
                    </tr>
                </thead>
                <tbody class="text-gray-700 text-sm font-light">
                    {% if products %}
                        {% for product in products %}
                            <tr class="border-b border-gray-200 hover:bg-gray-50">
                                <td class="py-3 px-6 text-left whitespace-nowrap">{{ product.id }}</td>
                                <td class="py-3 px-6 text-left">{{ product.name }}</td>
                                <td class="py-3 px-6 text-left">${{ "%.2f" | format(product.price) }}</td>
                                <td class="py-3 px-6 text-left">{{ product.description or 'N/A' }}</td>
                                <td class="py-3 px-6 text-center">
                                    <div class="flex item-center justify-center space-x-2">
                                        <a href="{{ url_for('edit_product', product_id=product.id) }}" 
                                           class="bg-yellow-500 hover:bg-yellow-600 text-white text-xs px-3 py-1 rounded-md transition duration-300">
                                            Edit
                                        </a>
                                        <a href="{{ url_for('delete_product', product_id=product.id) }}" 
                                           class="bg-red-500 hover:bg-red-600 text-white text-xs px-3 py-1 rounded-md transition duration-300"
                                           onclick="return confirm('Are you sure you want to delete this product?');">
                                            Delete
                                        </a>
                                    </div>
                                </td>
                            </tr>
                        {% endfor %}
                    {% else %}
                        <tr>
                            <td colspan="5" class="py-6 text-center text-gray-500">No products yet! Click "Add New Product" to create one.</td>
                        </tr>
                    {% endif %}
                </tbody>
            </table>
        </div>
        <a href="/" class="text-purple-500 hover:underline mt-6 block">Back to Home</a>
    </div>
</div>
{% endblock %}
```

#### `templates/add_product.html` (Add Product Form - SQLite)

```html
<!-- templates/add_product.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-purple-600 mb-6">{{ page_title }}</h1>
        
        <form method="POST" action="{{ url_for('add_product') }}" class="space-y-4">
            <input type="text" name="name" placeholder="Product Name" 
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500" required>
            <input type="number" name="price" placeholder="Price (e.g., 19.99)" step="0.01"
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500" required>
            <textarea name="description" placeholder="Product Description (Optional)" rows="4"
                      class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"></textarea>
            <button type="submit" 
                    class="w-full bg-purple-500 hover:bg-purple-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Save Product
            </button>
        </form>
        <a href="{{ url_for('products_list') }}" class="text-purple-500 hover:underline mt-4 block">Back to Products List</a>
    </div>
</div>
{% endblock %}
```

#### `templates/edit_product.html` (Edit Product Form - SQLite)

```html
<!-- templates/edit_product.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-yellow-600 mb-6">{{ page_title }}</h1>
        
        <form method="POST" action="{{ url_for('edit_product', product_id=product.id) }}" class="space-y-4">
            <input type="text" name="name" placeholder="Product Name" value="{{ product.name }}"
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500" required>
            <input type="number" name="price" placeholder="Price (e.g., 19.99)" step="0.01" value="{{ product.price }}"
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500" required>
            <textarea name="description" placeholder="Product Description (Optional)" rows="4"
                      class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500">{{ product.description or '' }}</textarea>
            <button type="submit" 
                    class="w-full bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Update Product
            </button>
        </form>
        <a href="{{ url_for('products_list') }}" class="text-yellow-500 hover:underline mt-4 block">Back to Products List</a>
    </div>
</div>
{% endblock %}
```

-----

### 5\. Run Your Flask Application

Follow these steps to get your Flask application up and running:

1.  **Open Your Terminal/Command Prompt:**
    Navigate to the `flask_crud_apps` directory (where your `app.py` file is located).

    ```bash
    cd flask_crud_apps
    ```

2.  **Set Flask Environment Variable:**
    You need to tell Flask which file contains your application.

      * **On Linux/macOS:**
        ```bash
        export FLASK_APP=app.py
        ```
      * **On Windows (Command Prompt):**
        ```bash
        set FLASK_APP=app.py
        ```
      * **On Windows (PowerShell):**
        ```powershell
        $env:FLASK_APP="app.py"
        ```

3.  **Initialize the Database (Important for SQLite part):**
    The `create_db()` function in `app.py` is set to run automatically when you start the app for the first time (`if __name__ == '__main__':`). This will create the `site.db` file and the `product` table. If you ever need to reset your database, you can delete `site.db` and restart the server.

4.  **Start the Flask Development Server:**

    ```bash
    flask run
    ```

    You should see output similar to this, indicating the server is running:

    ```
     * Serving Flask app 'app.py'
     * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```

-----

### 6\. Test Your Application

Open your web browser and go to `http://127.0.0.1:5000/`. You'll see the main menu with links to each of the CRUD applications:

  * **To-Do List (In-memory):**

      * Click "To-Do List" or go to `http://127.0.0.1:5000/todo`.
      * Add new tasks using the input field and "Add Task" button.
      * Click "Delete" next to a task to remove it.
      * *Note:* Tasks will disappear if you restart the Flask server, as they are stored in memory.

  * **Simple Notes App (In-memory):**

      * Click "Notes App" or go to `http://127.0.0.1:5000/notes`.
      * Click "Add New Note" to create a note with a title and content.
      * On the notes list, you can click "Edit" to modify an existing note or "Delete" to remove it.
      * *Note:* Notes will disappear if you restart the Flask server.

  * **Products (Flask + SQLite):**

      * Click "Products (SQLite)" or go to `http://127.0.0.1:5000/products`.
      * Click "Add New Product" to add products with a name, price, and optional description. These will be saved to `site.db`.
      * On the products list, you can click "Edit" to update product details or "Delete" to remove a product.
      * *Note:* Data in this section is persistent\! It will remain even if you restart the Flask server, as it's stored in the SQLite database file (`site.db`).

This comprehensive guide provides you with a solid foundation for building CRUD applications in Flask, moving from simple in-memory storage to a persistent database solution. Experiment with each part to understand the different approaches to data management.