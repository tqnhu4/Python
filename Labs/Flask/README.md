# 7-Day Flask Learning Roadmap

This roadmap focuses on practical application, building a small project by the end of the week.

## 📅 Day 1: Introduction to Flask & Setting Up
### Understanding Web Concepts:
- Briefly review how the web works (client-server model, HTTP methods like GET/POST).
- What is a web framework? Why Flask?
### Installation:
- Install Python (if you haven't already).
- Set up a virtual environment: python -m venv venv
- Activate the virtual environment: source venv/bin/activate (Linux/macOS) or .\venv\Scripts\activate (Windows)
- Install Flask: pip install Flask
### Your First Flask App:
- Create a simple hello.py file:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

- Run the app: python hello.py
- Understand @app.route(), app.run(), and debug=True.
### Practice:
- Create a few more basic routes with different return strings.

## 📅 Day 2: Routing, Templates, and Static Files
- **URL Routing & Variables:**
  - Learn how to define routes with dynamic parts: @app.route('/user/<username>')
  - Pass variables from the URL to your functions.
- **Jinja2 Templating:**
  - Introduction to Jinja2 syntax for rendering HTML.
  - Create a templates folder.
  - Use render_template():

```python
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('greeting.html', name=name)
```  
  - In templates/greeting.html:
```python
<!DOCTYPE html>
<html>
<head>
    <title>Greeting</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```  

- **Static Files:**
  - How to serve CSS, JavaScript, and images.
  - Create a static folder.
  - Link static files in your templates: <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
- **Practice:**
  - Create a simple "about" page using a template.
  - Add some basic CSS to your greeting.html.

## 📅 Day 3: Forms and Request Handling
- **HTML Forms:**
  - Understand <form> tags, method (GET/POST), and action.
- **Handling Form Submissions:**
  - Using request.method to distinguish between GET and POST requests.
  - Accessing form data with request.form:  
```python
from flask import request, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Basic validation
        if username == 'admin' and password == 'password':
            return 'Logged in successfully!'
        else:
            return 'Invalid credentials'
    return render_template('login.html')
```

  - redirect() and url_for().
- **Flash Messages (Optional but Recommended):**
  - Displaying one-time messages to the user: flash('Message here!')
  - Requiring session['SECRET_KEY'].
- **Practice:**
  - Create a simple contact form that takes name and email. Display the submitted data on a new page.  

## 📅 Day 4: Database Integration (SQLAlchemy ORM)
- **Introduction to Databases & ORMs:**
  - Why use a database? What is an ORM?
- **Flask-SQLAlchemy:**
  - Install: pip install Flask-SQLAlchemy
  - Configure database URI (e.g., SQLite for local development).
  - Define models (Python classes representing database tables):  

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```  

- **Database Operations (CRUD):**
  - Create tables: db.create_all() (run once).
  - Add new records: user = User(username='test', email='test@example.com'); db.session.add(user); db.session.commit()
  - Query records: User.query.all(), User.query.filter_by(username='test').first()
  - Update records: user.email = 'new@example.com'; db.session.commit()
  - Delete records: db.session.delete(user); db.session.commit()
- **Practice:**
  - Create a simple "Todo" application:
  - Define a Todo model with id, task, completed (boolean).
  - Create a route to add new todos.
  - Create a route to list all todos.

## 📅 Day 5: Building Out the Todo App (CRUD Operations)
- **Displaying Todos:**
  - Fetch all todos from the database and pass them to a template.
  - Use Jinja2 loops to display each todo item.
- **Adding New Todos:**
  - Implement the form for adding a new todo item.
  - Process the form submission and save the new todo to the database.
- **Marking Todos as Complete (Update):**
  - Add a way (e.g., a checkbox or a link) to mark a todo as completed.
  - Update the completed field in the database.
- **Deleting Todos:**
  - Add a delete button/link for each todo item.
  - Implement the route to delete a todo based on its ID.
- **Practice:**
  - Complete the full CRUD functionality for your Todo application.  

## 📅 Day 6: Blueprints and Project Structure
- **Why Blueprints?**
  - Organizing larger Flask applications.
  - Modularity and reusability.
- **Creating a Blueprint:**
  - Define a blueprint: from flask import Blueprint; my_blueprint = Blueprint('my_blueprint', __name__)
  - Register routes on the blueprint: @my_blueprint.route('/hello')
  - Register the blueprint with the app: app.register_blueprint(my_blueprint)
- **Project Structure for Larger Apps:**
  - app/
      - __init__.py (app creation, configurations)
      - routes.py (or blueprints/ directory for multiple blueprints)
      - models.py
      - templates/
      - static/
  - run.py (to run the app)
- **Practice:**
  - Refactor your Todo application to use a blueprint for its routes.
  - Organize your project into a more structured layout. 

## 📅 Day 7: Deployment & Next Steps
- **Basic Deployment Concepts:**
  - Difference between development server and production server.
  - Brief overview of WSGI servers (Gunicorn, uWSGI).
  - Using a simple Procfile for Heroku (optional, but a good starting point for cloud deployment).
- **Error Handling:**
  - Custom error pages: @app.errorhandler(404)
- **Configuration:**
  - Separate configuration for different environments (development, production).
- **Next Steps:**
  - User authentication (Flask-Login).
  - API development (Flask-RESTful).
  - Testing Flask applications.
  - Advanced templating (macros, inheritance).
- **Practice:**
  - Review your code.
  - Experiment with deploying your simple "Hello, World!" app to a free platform like Heroku (if you have time and an account).
  - Research one of the "Next Steps" topics.   