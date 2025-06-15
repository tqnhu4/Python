
## ✍️ Simple Blog System in Python

This project will create a basic web-based blog system where users can view, create, edit, and delete blog posts.

### Key Features:

* **Create Posts:** Add new blog entries.
* **View Posts:** Display all existing blog posts.
* **Edit Posts:** Modify existing blog entries.
* **Delete Posts:** Remove blog entries.
* **Data Persistence:** Store posts in a database.

### Technologies Used:

* **Python:** The programming language.
* **Flask:** A lightweight web framework for Python.
* **SQLite:** A file-based SQL database (simple to use for development).
* **HTML/CSS:** For basic front-end structure and styling.

### 📁 Project Structure

```
simple-blog-system/
├── app.py
├── database.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   └── edit.html
└── static/
    └── style.css
```

### 📋 Prerequisites

* Python 3.6+ installed
* Install Flask:
    ```bash
    pip install Flask
    ```

---

### 🚀 Step-by-Step Implementation

#### 1. Create `app.py` (Main Flask Application)

This file will contain our Flask application, handling routes, database interactions (via `database.py`), and rendering templates.

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import database
import datetime

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_here' # Change this to a strong, random key in production!

# Route for the homepage - displaying all posts
@app.route('/')
def index():
    posts = database.get_all_posts()
    return render_template('index.html', posts=posts)

# Route for creating a new post
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not title:
            flash('Title is required!', 'error')
        elif not content:
            flash('Content is required!', 'error')
        else:
            database.create_post(title, content, created_at)
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))
    return render_template('create.html')

# Route for editing an existing post
@app.route('/edit/<int:post_id>', methods=('GET', 'POST'))
def edit(post_id):
    post = database.get_post_by_id(post_id)

    if post is None:
        flash('Post not found!', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!', 'error')
        elif not content:
            flash('Content is required!', 'error')
        else:
            database.update_post(post_id, title, content)
            flash('Post updated successfully!', 'success')
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

# Route for deleting a post
@app.route('/delete/<int:post_id>', methods=('POST',))
def delete(post_id):
    post = database.get_post_by_id(post_id)
    if post is None:
        flash('Post not found!', 'error')
    else:
        database.delete_post(post_id)
        flash(f'Post "{post[1]}" deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    database.init_db() # Initialize the database when the app starts
    app.run(debug=True) # Run in debug mode for development (auto-reloads, useful errors)
```

#### 2. Create `database.py` (SQLite Database Operations)

This file will handle all interactions with the SQLite database. It will create the database file and table, and provide functions for CRUD (Create, Read, Update, Delete) operations on posts.

```python
# database.py
import sqlite3

DATABASE_NAME = 'blog.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row # Allows accessing columns by name
    return conn

def init_db():
    conn = get_db_connection()
    # Create posts table if it doesn't exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(f"[*] Database '{DATABASE_NAME}' initialized.")

def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()
    conn.close()
    return posts

def get_post_by_id(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return post

def create_post(title, content, created_at):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content, created_at) VALUES (?, ?, ?)',
                 (title, content, created_at))
    conn.commit()
    conn.close()

def update_post(post_id, title, content):
    conn = get_db_connection()
    conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                 (title, content, post_id))
    conn.commit()
    conn.close()

def delete_post(post_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
```

#### 3. Create `templates/` Directory and HTML Files

Create a directory named `templates` in the same level as `app.py` and `database.py`. Inside `templates`, create the following HTML files:

##### `templates/base.html` (Base Template)

This file defines the basic structure of our web pages, including common headers, navigation, and a place for flash messages. Other templates will "inherit" from this.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Blog{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <h1>A Simple Blog</h1>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('create') }}">New Post</a></li>
        </ul>
    </nav>
    <hr>
    <div class="content">
        {% for message in get_flashed_messages(with_categories=true) %}
            <div class="flash flash-{{ message[0] }}">
                {{ message[1] }}
            </div>
        {% endfor %}
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

##### `templates/index.html` (Homepage - Displaying Posts)

This page displays all blog posts fetched from the database.

```html
{% extends 'base.html' %}

{% block title %}All Posts{% endblock %}

{% block content %}
    <h2>All Blog Posts</h2>
    {% if not posts %}
        <p>No posts yet. <a href="{{ url_for('create') }}">Create one!</a></p>
    {% else %}
        {% for post in posts %}
            <div class="post">
                <h3>{{ post['title'] }}</h3>
                <p class="post-meta">Posted on: {{ post['created_at'] }}</p>
                <p>{{ post['content'] }}</p>
                <a href="{{ url_for('edit', post_id=post['id']) }}" class="button">Edit</a>
                <form action="{{ url_for('delete', post_id=post['id']) }}" method="POST" style="display:inline;">
                    <input type="submit" value="Delete" class="button button-delete" onclick="return confirm('Are you sure you want to delete this post?');">
                </form>
            </div>
        {% endfor %}
    {% endif %}
{% endblock %}
```

##### `templates/create.html` (Create New Post Form)

This page provides a form to create a new blog post.

```html
{% extends 'base.html' %}

{% block title %}Create New Post{% endblock %}

{% block content %}
    <h2>Create a New Blog Post</h2>
    <form method="POST">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" required><br><br>

        <label for="content">Content:</label><br>
        <textarea id="content" name="content" rows="10" required></textarea><br><br>

        <input type="submit" value="Submit Post" class="button">
    </form>
{% endblock %}
```

##### `templates/edit.html` (Edit Existing Post Form)

This page provides a form to edit an existing blog post, pre-filled with its current data.

```html
{% extends 'base.html' %}

{% block title %}Edit Post{% endblock %}

{% block content %}
    <h2>Edit Blog Post</h2>
    {% if post %}
        <form method="POST">
            <label for="title">Title:</label><br>
            <input type="text" id="title" name="title" value="{{ post['title'] }}" required><br><br>

            <label for="content">Content:</label><br>
            <textarea id="content" name="content" rows="10" required>{{ post['content'] }}</textarea><br><br>

            <input type="submit" value="Update Post" class="button">
        </form>
    {% else %}
        <p>Post not found.</p>
    {% endif %}
{% endblock %}
```

#### 4. Create `static/` Directory and `style.css` (Basic Styling)

Create a directory named `static` in the same level as `app.py`. Inside `static`, create `style.css` for basic visual appeal.

```css
/* static/style.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}

nav {
    background-color: #333;
    color: white;
    padding: 1em;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav h1 {
    margin: 0;
    color: white;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav ul li {
    display: inline;
    margin-left: 20px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

hr {
    border: 0;
    border-top: 1px solid #ccc;
    margin: 1em 0;
}

.content {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.post {
    border-bottom: 1px solid #eee;
    padding-bottom: 15px;
    margin-bottom: 15px;
}

.post:last-child {
    border-bottom: none;
}

.post h3 {
    color: #0056b3;
    margin-top: 0;
    margin-bottom: 5px;
}

.post-meta {
    font-size: 0.9em;
    color: #777;
    margin-bottom: 10px;
}

.button {
    display: inline-block;
    background-color: #007bff;
    color: white;
    padding: 8px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    text-decoration: none;
    margin-right: 10px;
}

.button:hover {
    background-color: #0056b3;
}

.button-delete {
    background-color: #dc3545;
}

.button-delete:hover {
    background-color: #c82333;
}

form label {
    font-weight: bold;
    margin-bottom: 5px;
}

form input[type="text"],
form textarea {
    width: 98%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.flash {
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 4px;
}

.flash-success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.flash-error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}
```

---

### ▶️ How to Run the Application

1.  **Navigate to your project directory** (`simple-blog-system/`) in your terminal.
2.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    You should see output similar to this:
    ```
     [*] Database 'blog.db' initialized.
     * Serving Flask app 'app'
     * Debug mode: on
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
     Press CTRL+C to quit
    ```
3.  **Open your web browser** and go to `http://127.0.0.1:5000`.

### 🧪 How to Test

1.  **Homepage:** You'll initially see an empty blog with a message "No posts yet. Create one!".
2.  **Create a Post:**
    * Click on "New Post" in the navigation bar or the "Create one!" link.
    * Enter a **Title** and **Content** for your post.
    * Click "Submit Post".
    * You should be redirected to the homepage, and your new post will appear with a success flash message.
3.  **Create More Posts:** Add a few more posts to see them listed.
4.  **Edit a Post:**
    * On the homepage, next to a post, click the "Edit" button.
    * Modify the title or content.
    * Click "Update Post".
    * You'll be redirected back to the homepage with the updated post and a success message.
5.  **Delete a Post:**
    * On the homepage, next to a post, click the "Delete" button.
    * Confirm the deletion in the pop-up.
    * The post will be removed from the list, and you'll see a success flash message.
6.  **Error Handling (Missing Fields):**
    * Try creating or editing a post with an empty title or content. You should see an error flash message.

---

### 📝 Code Explanation

#### `app.py`

* **`Flask(__name__)`**: Initializes the Flask application.
* **`app.secret_key`**: Essential for securely handling sessions and flash messages. **Change this to a long, random string in a real application!**
* **`@app.route('/')`, `@app.route('/create')`, etc.**: These are **decorators** that map URL paths to Python functions. When a browser requests that URL, the corresponding function is executed.
* **`render_template()`**: Flask function to render HTML templates. It automatically looks for templates in the `templates/` folder.
* **`request.method`**: Checks if the HTTP request is `GET` (for displaying the form) or `POST` (for submitting data).
* **`request.form['field_name']`**: Accesses data submitted through HTML forms.
* **`redirect(url_for('function_name'))`**: Redirects the user to a different URL after an action (e.g., after creating a post). `url_for` is used to build URLs dynamically.
* **`flash()` and `get_flashed_messages()`**: Flask's built-in mechanism for displaying one-time messages to the user (e.g., "Post created successfully!").

#### `database.py`

* **`sqlite3.connect('blog.db')`**: Connects to an SQLite database file named `blog.db`. If the file doesn't exist, SQLite will create it.
* **`conn.row_factory = sqlite3.Row`**: This is a very useful setting! It makes database rows behave like dictionaries, allowing you to access columns by name (e.g., `post['title']`) instead of by index (`post[0]`).
* **`CREATE TABLE IF NOT EXISTS`**: SQL command to create the `posts` table if it doesn't already exist.
    * `id INTEGER PRIMARY KEY AUTOINCREMENT`: Automatically generates unique IDs for each post.
    * `TEXT NOT NULL`: Ensures these fields cannot be empty.
    * `created_at TEXT DEFAULT CURRENT_TIMESTAMP`: Automatically sets the creation time if not provided. We explicitly set it in `app.py` to ensure consistent formatting.
* **`conn.execute()`**: Executes SQL queries. Parameterized queries (using `?` placeholders) are used to prevent **SQL injection vulnerabilities**.
* **`conn.commit()`**: Saves the changes made to the database.
* **`conn.close()`**: Closes the database connection. **Always close connections when you're done with them.**
* **`fetchall()`**: Retrieves all matching rows from a `SELECT` query.
* **`fetchone()`**: Retrieves only the first matching row.

#### HTML Templates (`templates/`)

* **`{% extends 'base.html' %}`**: Jinja2 (Flask's default templating engine) syntax to inherit from `base.html`.
* **`{% block title %}{% endblock %}` and `{% block content %}{% endblock %}`**: These are **blocks** defined in `base.html` that can be overridden by child templates.
* **`{{ variable }}`**: Jinja2 syntax to display Python variables passed from the Flask application.
* **`{{ url_for('static', filename='style.css') }}`**: Generates the correct URL for static files (like CSS).
* **`{% for item in list %}{% endfor %}`**: Jinja2 loop to iterate over data (e.g., `posts`).
* **`{{ post['id'] }}`**: Accesses specific fields of a post object (which is a `sqlite3.Row` object, behaving like a dictionary).
* **`onclick="return confirm(...)"`**: A simple JavaScript way to ask for user confirmation before deleting.

---

### ⚠️ Limitations & Future Improvements (Moving to Advanced)

This is a **simple** blog system. For a real-world application, you would need to add:

* **User Authentication:** Users can log in, create their own posts, and only edit/delete their posts. This would involve:
    * User registration and login forms.
    * Hashing passwords (e.g., with `bcrypt`).
    * Session management.
* **Rich Text Editor:** Instead of a simple `textarea`, integrate a WYSIWYG editor (e.g., TinyMCE, CKEditor) for post content.
* **Comments:** Allow users to comment on posts.
* **Pagination:** For many posts, you'd need to paginate the display on the homepage.
* **Tags/Categories:** Organize posts with tags or categories.
* **Search Functionality:** A search bar to find posts.
* **Deployment:** Learn how to deploy a Flask application to a production server (e.g., with Gunicorn/Nginx, Docker, or platforms like Heroku/AWS Elastic Beanstalk).
* **More Robust Database:** For larger scale, consider PostgreSQL or MySQL instead of SQLite. Use an ORM like SQLAlchemy for more abstract and powerful database interactions.
* **Error Pages:** Custom 404, 500 error pages.
* **Frontend Framework:** For more interactive UIs, consider integrating a JavaScript framework like React, Vue, or Angular.

This project provides a solid foundation for building web applications with Flask and Python!