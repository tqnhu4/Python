# app.py
from flask import Flask, render_template

# Initialize the Flask application
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses it to locate resources like templates and static files.
app = Flask(__name__)

# Exercise 1 & 2: Hello Flask! and Display Multiple Routes
# Route for the home page. This function will be executed when a user navigates to the root URL.
# Example URL: http://127.0.0.1:5000/
@app.route('/')
def home():
    return "Hello, Flask! Welcome to the Home Page!"

# Route for the about page.
# Example URL: http://127.0.0.1:5000/about
@app.route('/about')
def about():
    return 'This is the About Page. Learn more about us!'

# Route for the contact page.
# Example URL: http://127.0.0.1:5000/contact
@app.route('/contact')
def contact():
    return 'Contact us at contact@example.com'

# Exercise 3 & 4: Render Basic HTML and Pass Data from Route into HTML
# Route to render an HTML template and pass data to it.
# Example URL: http://127.0.0.1:5000/html_page
@app.route('/html_page')
def show_html_page():
    # A variable to be passed to the HTML template
    message = "This message is from Flask!"
    # render_template looks for 'index.html' inside the 'templates' folder.
    # It passes the 'message' variable to the template, where it can be displayed.
    return render_template('index.html', flask_message=message, page_title="Dynamic HTML Page")

# Exercise 5: Read Data from URL
# Route to display a user's greeting based on a dynamic URL segment.
# The '<username>' part in the route decorator captures the value from the URL
# and passes it as an argument to the 'greet_user' function.
# Example URL: http://127.0.0.1:5000/user/John or http://127.0.0.1:5000/user/Alice
@app.route('/user/<username>')
def greet_user(username):
    # Render the 'user.html' template and pass the captured username.
    return render_template('user.html', user_name=username, page_title=f"Hello {username}!")

# This block ensures the Flask development server runs only when the script is executed directly.
if __name__ == '__main__':
    # app.run() starts the development server.
    # debug=True enables debug mode, which provides helpful error messages
    # and automatically reloads the server when code changes, which is great for development.
    app.run(debug=True)