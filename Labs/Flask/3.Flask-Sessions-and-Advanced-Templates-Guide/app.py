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