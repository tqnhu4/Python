
# Basic Flask Application Guide

This guide will walk you through creating a simple Flask web application from scratch. You'll learn how to set up routes, display basic text and HTML, pass data to your web pages, and even read information directly from the URL.

-----

### 1\. Project Setup

Let's start by getting your development environment ready.

1.  **Install Flask:**
    First, open your terminal or command prompt. If you don't have Flask installed, run this command:

    ```bash
    pip install Flask
    ```

2.  **Create Your Project Folder:**
    Make a new directory for your Flask application. We'll call it `my_first_flask_app`.

    ```bash
    mkdir my_first_flask_app
    cd my_first_flask_app
    ```

3.  **Create `app.py`:**
    Inside `my_first_flask_app`, create a Python file named `app.py`. This is where all your Flask application logic will go.

4.  **Create `templates` Folder:**
    Flask needs a special folder to find your HTML files. Inside `my_first_flask_app`, create a new folder called `templates`.

    ```bash
    mkdir templates
    ```

5.  **Create HTML Files:**
    Now, inside the `templates` folder, create these four empty HTML files. We'll fill them with content shortly.

      * `index.html`
      * `about.html`
      * `contact.html`
      * `user.html`

-----

### 2\. Application Code (`app.py`)

Copy and paste this entire Python code block into your `app.py` file. Each section corresponds to one of the Flask learning objectives.

```python
# app.py
from flask import Flask, render_template

# Initialize the Flask application
# Flask uses '__name__' to know where to look for resources like template files.
app = Flask(__name__)

# --- Hello Flask! & Display Multiple Routes ---

# This is the default route for your website (e.g., http://127.0.0.1:5000/)
# It simply returns a string.
@app.route('/')
def home():
    return "Hello, Flask! Welcome to the Home Page!"

# This route handles requests to /about (e.g., http://127.0.0.1:5000/about)
# It returns a different string.
@app.route('/about')
def about():
    return 'This is the About Page. We build awesome web apps with Flask!'

# This route handles requests to /contact (e.g., http://127.0.0.1:5000/contact)
# It also returns a simple string response.
@app.route('/contact')
def contact():
    return 'Feel free to contact us at support@myflaskapp.com'

# --- Render Basic HTML & Pass Data to HTML ---

# This route will demonstrate rendering an HTML file and passing data to it.
# Example URL: http://127.0.0.1:5000/html_example
@app.route('/html_example')
def html_example():
    # Define some data we want to send to our HTML template.
    dynamic_content = "This content comes from your Flask application!"
    current_year = 2025 # Just an example of another variable

    # render_template() looks for the specified HTML file ('index.html' here)
    # inside your 'templates' folder.
    # We pass Python variables as keyword arguments (e.g., 'message=dynamic_content').
    # These become available in the HTML using Jinja2 syntax (e.g., {{ message }}).
    return render_template('index.html', message=dynamic_content, year=current_year, page_title="My Dynamic Flask Page")

# --- Read Data from URL ---

# This route shows how to capture parts of the URL as variables.
# The '<username>' part is a variable placeholder. Whatever text appears there
# in the URL will be captured and passed as the 'username' argument to the function.
# Example URLs: http://127.0.0.1:5000/user/john or http://127.0.0.1:5000/user/jane_doe
@app.route('/user/<username>')
def show_user_profile(username):
    # Instead of just returning a plain string, we'll render an HTML template
    # and pass the captured username to it.
    return render_template('user.html', user_name=username, page_title=f"Welcome {username}!")

# This block is standard for running Flask apps in development.
# It makes sure 'app.run()' is called only when you execute the script directly.
if __name__ == '__main__':
    # app.run() starts the development server.
    # debug=True automatically reloads the server on code changes and provides helpful error messages.
    app.run(debug=True)
```

-----

### 3\. HTML Template Files (`templates` folder)

Now, copy and paste these HTML codes into their respective files inside your `templates` folder. These files use **Jinja2**, Flask's default templating engine, which lets you embed Python-like expressions (`{{ variable }}`) directly into your HTML. Basic Tailwind CSS is included for some quick styling.

#### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-blue-600 mb-4">{{ page_title }}</h1>
        <p class="text-gray-700 text-lg mb-6">
            This page is rendered from an HTML file using Flask's `render_template` function!
        </p>
        <p class="text-green-600 font-semibold text-xl mb-8">
            Here's the message from your Flask app: <br> "{{ message }}"
        </p>
        <p class="text-gray-500 text-sm">
            Current year: {{ year }}
        </p>
        <div class="mt-8 space-y-4">
            <a href="/" class="block bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
                Go to Home (Text)
            </a>
            <a href="/about" class="block bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
                Go to About (Text)
            </a>
            <a href="/contact" class="block bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
                Go to Contact (Text)
            </a>
            <a href="/user/Alice" class="block bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
                Visit User Profile (Alice)
            </a>
        </div>
    </div>
</body>
</html>
```

#### `templates/about.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About This App</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-green-600 mb-4">About Our Simple Flask App</h1>
        <p class="text-gray-700 text-lg mb-6">
            This application is built purely for learning purposes, demonstrating basic Flask functionalities.
        </p>
        <a href="/" class="block bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
            Back to Home
        </a>
    </div>
</body>
</html>
```

#### `templates/contact.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-purple-600 mb-4">Get in Touch!</h1>
        <p class="text-gray-700 text-lg mb-6">
            For inquiries, please email us at: <br>
            <span class="text-blue-500 font-semibold">info@myflaskapp.com</span>
        </p>
        <a href="/" class="block bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
            Back to Home
        </a>
    </div>
</body>
</html>
```

#### `templates/user.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-orange-600 mb-4">Hello, <span class="text-blue-500">{{ user_name }}</span>!</h1>
        <p class="text-gray-700 text-lg mb-6">
            You've reached a personalized page! The name "{{ user_name }}" was dynamically read from the URL.
        </p>
        <a href="/" class="block bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
            Back to Home
        </a>
    </div>
</body>
</html>
```

-----

### 4\. Run Your Flask Application

Alright, time to see your app in action\!

1.  **Open Your Terminal/Command Prompt:** Make sure you're in the `my_first_flask_app` directory (the one containing `app.py` and the `templates` folder).

    ```bash
    cd my_first_flask_app
    ```

2.  **Tell Flask Your App File:** Before running, you need to set an environment variable so Flask knows which file contains your app.

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

3.  **Start the Flask Server:**

    ```bash
    flask run
    ```

    You'll see output confirming the server is running, usually on `http://127.0.0.1:5000/`.

-----

### 5\. Test Your Application

Open your web browser and navigate to these URLs to see each feature in action:

  * **`http://127.0.0.1:5000/`**: You'll see the "Hello, Flask\! Welcome to the Home Page\!" text.
  * **`http://127.0.0.1:5000/about`**: This shows the "About" page text.
  * **`http://127.0.0.1:5000/contact`**: This shows the "Contact" page text.
  * **`http://127.0.0.1:5000/html_example`**: This will load `index.html` and show the dynamic message passed from your Flask app.
  * **`http://127.0.0.1:5000/user/YourName`**: Replace `YourName` with anything you like (e.g., `http://127.0.0.1:5000/user/JaneDoe`). This loads `user.html` and greets you by the name you entered in the URL\!

That's it\! You've successfully built and run a Flask application demonstrating basic routing, HTML rendering, data passing, and URL parameter handling. This is a fantastic start to web development with Python\!