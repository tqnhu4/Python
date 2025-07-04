# Flask Sessions and Advanced Templates Guide (Level 3)

This guide will teach you how to enhance your Flask applications by using sessions to store user data across requests, implementing logout functionality, and structuring your HTML templates using inheritance for better organization.

-----

### 1\. Project Setup

Let's prepare your development environment for this new application.

1.  **Install Flask:**
    If you haven't already, open your terminal or command prompt and install Flask:

    ```bash
    pip install Flask
    ```

2.  **Create Your Project Folder:**
    Create a new directory for this Flask application. Let's call it `flask_sessions_app`.

    ```bash
    mkdir flask_sessions_app
    cd flask_sessions_app
    ```

3.  **Create `app.py`:**
    Inside `flask_sessions_app`, create a Python file named `app.py`. This will contain all your Flask application's backend code.

4.  **Create `templates` Folder:**
    Flask needs a dedicated folder for your HTML template files. Create a new folder named `templates` inside `flask_sessions_app`.

    ```bash
    mkdir templates
    ```

5.  **Create HTML Files:**
    Inside the `templates` folder, create the following empty HTML files. These will be used to demonstrate template inheritance and session data.

      * `base.html`
      * `login.html`
      * `dashboard.html`
      * `profile.html`

-----

### 2\. Application Code (`app.py`)

Copy and paste this entire Python code block into your `app.py` file. Pay close attention to how `session` is used to store and retrieve user data, and how `redirect` and `url_for` are used for navigation.

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

# --- IMPORTANT: Secret Key for Sessions ---
# Flask sessions require a secret key to encrypt the session cookie.
# In a real application, this should be a long, random string
# and stored securely (e.g., in an environment variable).
app.secret_key = 'your_super_secret_key_here_replace_me_in_production'

# A simple "database" for demonstration purposes
USERS = {
    "admin": "password123",
    ""user"": "pass"
}

# --- Main Index Page ---
@app.route('/')
def index():
    # The index page will simply redirect to the dashboard if logged in,
    # or to the login page if not.
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# --- Exercise 1: Store Username in Session (Login) ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        # If already logged in, redirect to dashboard
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            session['username'] = username  # Store username in session
            flash('Logged in successfully!', 'success') # Optional: Flash message
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'error') # Optional: Flash message
    return render_template('login.html', page_title="Login")

# --- Exercise 2: Logout Functionality ---
@app.route('/logout')
def logout():
    session.pop('username', None) # Remove username from session
    flash('You have been logged out.', 'info') # Optional: Flash message
    return redirect(url_for('login'))

# --- Dashboard Page (displays session data) ---
@app.route('/dashboard')
def dashboard():
    # Check if user is logged in (username exists in session)
    if 'username' not in session:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('login'))
    
    # Pass the username from the session to the template
    return render_template('dashboard.html', 
                           page_title="Dashboard", 
                           user_name=session['username'])

# --- Another Page (displays session data) ---
@app.route('/profile')
def profile():
    # This page also requires login to access
    if 'username' not in session:
        flash('Please log in to view your profile.', 'warning')
        return redirect(url_for('login'))
    
    # Pass the username from the session to the template
    return render_template('profile.html', 
                           page_title="User Profile", 
                           user_name=session['username'])


# This block ensures the Flask development server runs only when the script is executed directly.
if __name__ == '__main__':
    app.run(debug=True)
```

-----

### 3\. HTML Template Files (`templates` folder)

These HTML files demonstrate template inheritance and how to display session data. Jinja2 syntax (`{% ... %}` for control flow and `{{ ... }}` for variables) is used. Tailwind CSS is included for basic styling.

#### `templates/base.html` (Base Template)

This template defines the common structure for all your pages, including the head, a navigation bar, and blocks where child templates can insert their specific content.

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %} - Flask App</title>
    <!-- Tailwind CSS CDN for quick styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex flex-col">
    <nav class="bg-blue-600 p-4 text-white shadow-md">
        <div class="container mx-auto flex justify-between items-center">
            <a href="/" class="text-2xl font-bold hover:text-blue-200 transition duration-300">My Flask App</a>
            <ul class="flex space-x-6">
                {% if session.username %}
                    <li><a href="/dashboard" class="hover:text-blue-200 transition duration-300">Dashboard</a></li>
                    <li><a href="/profile" class="hover:text-blue-200 transition duration-300">Profile</a></li>
                    <li><span class="text-blue-200">Hello, {{ session.username }}!</span></li>
                    <li><a href="/logout" class="bg-red-500 hover:bg-red-600 px-3 py-1 rounded-md transition duration-300">Logout</a></li>
                {% else %}
                    <li><a href="/login" class="hover:text-blue-200 transition duration-300">Login</a></li>
                {% endif %}
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
        <p>&copy; 2025 My Flask App. All rights reserved.</p>
    </footer>
</body>
</html>
```

#### `templates/login.html` (Login Page)

This template extends `base.html` and provides the login form.

```html
<!-- templates/login.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-purple-600 mb-6">Login</h1>
        
        <form method="POST" action="{{ url_for('login') }}" class="space-y-4">
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
    </div>
</div>
{% endblock %}
```

#### `templates/dashboard.html` (Dashboard Page)

This template extends `base.html` and displays the logged-in username.

```html
<!-- templates/dashboard.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-blue-600 mb-6">Welcome to Your Dashboard, {{ user_name }}!</h1>
        <p class="text-lg text-gray-700 mb-8">This is your personalized dashboard. You are logged in.</p>
        <p class="text-md text-gray-600">Explore other pages like your <a href="{{ url_for('profile') }}" class="text-blue-500 hover:underline">profile</a>.</p>
    </div>
</div>
{% endblock %}
```

#### `templates/profile.html` (Profile Page)

This is another page that extends `base.html` and shows the username from the session.

```html
<!-- templates/profile.html -->
{% extends "base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<div class="flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-green-600 mb-6">Your Profile, {{ user_name }}</h1>
        <p class="text-lg text-gray-700 mb-8">This is your profile page. Your username is retrieved from the session.</p>
        <p class="text-md text-gray-600">You can add more profile details here.</p>
    </div>
</div>
{% endblock %}
```

-----

### 4\. Run Your Flask Application

Follow these steps to get your Flask application up and running:

1.  **Open Your Terminal/Command Prompt:**
    Navigate to the `flask_sessions_app` directory (where your `app.py` file is located).

    ```bash
    cd flask_sessions_app
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

Open your web browser and go to `http://127.0.0.1:5000/`.

1.  **Initial Access:**
    You will be automatically redirected to the `/login` page because you're not yet logged in.

2.  **Login:**

      * Use the hint: `username: admin`, `password: password123` or `username: user`, `password: pass`.
      * Enter the credentials and click "Login".
      * You should be redirected to the `/dashboard` page, and you'll see a "Logged in successfully\!" flash message. The navigation bar will now display "Hello, [Your Username]\!" and a "Logout" button.

3.  **Navigate with Session Data:**

      * From the dashboard, click on "Profile" in the navigation bar. You should be taken to the `/profile` page, and it will also greet you by your username, demonstrating that the session data is available across different pages.
      * You can also try directly accessing `http://127.0.0.1:5000/dashboard` or `http://127.0.0.1:5000/profile` after logging in.

4.  **Logout:**

      * Click the "Logout" button in the navigation bar.
      * You will be redirected back to the `/login` page, and a "You have been logged out." flash message will appear. The navigation bar will revert to showing only the "Login" link.
      * Try accessing `/dashboard` or `/profile` now; you should be redirected back to the login page.

This application demonstrates the power of Flask sessions for maintaining user state and the efficiency of template inheritance for building consistent web layouts.