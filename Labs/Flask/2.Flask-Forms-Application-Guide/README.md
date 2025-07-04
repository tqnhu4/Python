
# Flask Forms Application Guide (Level 2)

This guide will teach you how to create Flask applications that interact with HTML forms. You'll learn to handle user input, perform calculations, implement simple login logic, and add basic form validation.

-----

### 1\. Project Setup

Let's prepare your development environment.

1.  **Install Flask:**
    If you haven't already, open your terminal or command prompt and install Flask:

    ```bash
    pip install Flask
    ```

2.  **Create Your Project Folder:**
    Create a new directory for this Flask application. Let's call it `flask_forms_app`.

    ```bash
    mkdir flask_forms_app
    cd flask_forms_app
    ```

3.  **Create `app.py`:**
    Inside `flask_forms_app`, create a Python file named `app.py`. This will contain all your Flask application's backend code.

4.  **Create `templates` Folder:**
    Flask needs a dedicated folder for your HTML template files. Create a new folder named `templates` inside `flask_forms_app`.

    ```bash
    mkdir templates
    ```

5.  **Create HTML Files:**
    Inside the `templates` folder, create the following empty HTML files. We'll fill them with content for each exercise.

      * `user_form.html`
      * `sum_form.html`
      * `login_form.html`
      * `dashboard.html`
      * `validation_form.html`

-----

### 2\. Application Code (`app.py`)

Copy and paste this entire Python code block into your `app.py` file. This file will contain all the Flask routes and logic for handling your forms.

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Exercise 1: User Name Input Form ---

@app.route('/greet_user', methods=['GET', 'POST'])
def greet_user_form():
    if request.method == 'POST':
        # Get the 'username' from the submitted form data
        user_name = request.form['username']
        # Render the same template, but now pass the username to display the greeting
        return render_template('user_form.html', greeting_message=f"Hello, {user_name}!")
    # If it's a GET request, just render the form without a greeting
    return render_template('user_form.html', greeting_message="")

# --- Exercise 2: Sum of Two Numbers Form ---

@app.route('/calculate_sum', methods=['GET', 'POST'])
def calculate_sum_form():
    result = None
    if request.method == 'POST':
        try:
            # Get numbers from the form and convert them to floats
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except ValueError:
            result = "Invalid input. Please enter valid numbers."
    # Render the form, passing the result (which might be None initially)
    return render_template('sum_form.html', sum_result=result)

# --- Exercise 3: Simple Login Form ---

# A simple "database" for demonstration purposes
USERS = {
    "admin": "password123",
    "user": "pass"
}

@app.route('/login', methods=['GET', 'POST'])
def login_form():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username exists and password matches
        if username in USERS and USERS[username] == password:
            # On successful login, redirect to the dashboard
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid username or password. Please try again."
    # Render the login form, passing any error message
    return render_template('login_form.html', error=error)

@app.route('/dashboard')
def dashboard():
    # This page is accessible after successful login
    return render_template('dashboard.html')

# --- Exercise 4: Form with Data Validation ---

@app.route('/validate_input', methods=['GET', 'POST'])
def validate_input_form():
    message = None
    if request.method == 'POST':
        user_input = request.form['input_field']
        if not user_input.strip(): # Check if the input is empty or just whitespace
            message = "Error: Input field cannot be empty!"
        else:
            message = f"Success! You entered: '{user_input}'"
    # Render the form, passing the message (error or success)
    return render_template('validation_form.html', validation_message=message)

# Main route to display links to all exercises
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Forms Exercises</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 flex items-center justify-center min-h-screen">
        <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
            <h1 class="text-3xl font-bold text-blue-700 mb-6">Flask Forms Exercises (Level 2)</h1>
            <ul class="space-y-4">
                <li><a href="/greet_user" class="block bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">1. User Name Input Form</a></li>
                <li><a href="/calculate_sum" class="block bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">2. Sum of Two Numbers Form</a></li>
                <li><a href="/login" class="block bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">3. Simple Login Form</a></li>
                <li><a href="/validate_input" class="block bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">4. Form with Data Validation</a></li>
            </ul>
        </div>
    </body>
    </html>
    """

# This block ensures the Flask development server runs only when the script is executed directly.
if __name__ == '__main__':
    app.run(debug=True)
```

-----

### 3\. HTML Template Files (`templates` folder)

Create these HTML files in your `templates` folder. They use **Jinja2** syntax (`{{ variable }}`) to display data passed from Flask and include Tailwind CSS for basic styling.

#### `templates/user_form.html`

```html
<!-- templates/user_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Name Form</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-blue-600 mb-6">Enter Your Name</h1>
        
        <!-- Display greeting message if available -->
        {% if greeting_message %}
            <p class="text-green-600 text-xl font-semibold mb-4">{{ greeting_message }}</p>
        {% endif %}

        <form method="POST" action="/greet_user" class="space-y-4">
            <input type="text" name="username" placeholder="Your Name" 
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required>
            <button type="submit" 
                    class="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Submit
            </button>
        </form>
        <a href="/" class="text-blue-500 hover:underline mt-4 block">Back to Home</a>
    </div>
</body>
</html>
```

#### `templates/sum_form.html`

```html
<!-- templates/sum_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sum Two Numbers</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-green-600 mb-6">Calculate Sum of Two Numbers</h1>
        
        <!-- Display sum result if available -->
        {% if sum_result is not none %}
            <p class="text-green-600 text-xl font-semibold mb-4">Result: {{ sum_result }}</p>
        {% endif %}

        <form method="POST" action="/calculate_sum" class="space-y-4">
            <input type="number" name="num1" placeholder="First Number" step="any"
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500" required>
            <input type="number" name="num2" placeholder="Second Number" step="any"
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500" required>
            <button type="submit" 
                    class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Calculate Sum
            </button>
        </form>
        <a href="/" class="text-green-500 hover:underline mt-4 block">Back to Home</a>
    </div>
</body>
</html>
```

#### `templates/login_form.html`

```html
<!-- templates/login_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Login</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-purple-600 mb-6">Login</h1>
        
        <!-- Display error message if available -->
        {% if error %}
            <p class="text-red-500 text-lg mb-4">{{ error }}</p>
        {% endif %}

        <form method="POST" action="/login" class="space-y-4">
            <input type="text" name="username" placeholder="Username" 
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500" required>
            <input type="password" name="password" placeholder="Password" 
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500" required>
            <button type="submit" 
                    class="w-full bg-purple-500 hover:bg-purple-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Login
            </button>
        </form>
        <p class="text-gray-500 text-sm mt-4">Hint: username 'admin', password 'password123' or username 'user', password 'pass'</p>
        <a href="/" class="text-purple-500 hover:underline mt-4 block">Back to Home</a>
    </div>
</body>
</html>
```

#### `templates/dashboard.html`

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-blue-600 mb-6">Welcome to the Dashboard!</h1>
        <p class="text-lg text-gray-700 mb-8">You have successfully logged in.</p>
        <a href="/login" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
            Logout
        </a>
        <a href="/" class="text-blue-500 hover:underline mt-4 block">Back to Home</a>
    </div>
</body>
</html>
```

#### `templates/validation_form.html`

```html
<!-- templates/validation_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Validation</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-yellow-600 mb-6">Form with Data Validation</h1>
        
        <!-- Display message (error or success) -->
        {% if validation_message %}
            {% if "Error" in validation_message %}
                <p class="text-red-500 text-lg mb-4">{{ validation_message }}</p>
            {% else %}
                <p class="text-green-600 text-lg mb-4">{{ validation_message }}</p>
            {% endif %}
        {% endif %}

        <form method="POST" action="/validate_input" class="space-y-4">
            <input type="text" name="input_field" placeholder="Enter something..." 
                   class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500">
            <button type="submit" 
                    class="w-full bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-3 px-4 rounded-md transition duration-300">
                Submit
            </button>
        </form>
        <a href="/" class="text-yellow-500 hover:underline mt-4 block">Back to Home</a>
    </div>
</body>
</html>
```

-----

### 4\. Run Your Flask Application

Follow these steps to get your Flask application up and running:

1.  **Open Your Terminal/Command Prompt:**
    Navigate to the `flask_forms_app` directory (where your `app.py` file is located).

    ```bash
    cd flask_forms_app
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

3.  **Start the Flask Development Server:**

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

### 5\. Test Your Application

Open your web browser and go to `http://127.0.0.1:5000/`. You'll see a simple index page with links to each exercise:

  * **1. User Name Input Form:** Click this link or go to `http://127.0.0.1:5000/greet_user`. Enter a name and submit to see the greeting.
  * **2. Sum of Two Numbers Form:** Click this link or go to `http://127.0.0.1:5000/calculate_sum`. Enter two numbers and submit to see their sum. Try entering non-numeric values to see the error handling.
  * **3. Simple Login Form:** Click this link or go to `http://127.0.0.1:5000/login`.
      * Try invalid credentials first (e.g., `wrong`/`wrong`).
      * Then, use the hint: `username: admin`, `password: password123` or `username: user`, `password: pass`. On successful login, you'll be redirected to the Dashboard.
  * **4. Form with Data Validation:** Click this link or go to `http://127.0.0.1:5000/validate_input`.
      * Try submitting an empty field.
      * Then, enter some text and submit to see the success message.

This setup provides a complete, runnable Flask application demonstrating how to work with various types of forms. Experiment with it to understand how Flask handles `GET` and `POST` requests, retrieves form data, and renders dynamic content.