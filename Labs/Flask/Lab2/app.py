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