from flask import Flask, render_template, request, redirect, flash
import smtplib
import os
import json
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # for flash messages
load_dotenv()

# Load project data
def load_projects():
    with open('data/projects.json') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    projects = load_projects()
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            send_email(name, email, message)
            flash("Message sent successfully!", "success")
        except:
            flash("An error occurred while sending the message.", "danger")
        
        return redirect('/contact')
    
    return render_template('contact.html')

def send_email(name, email, message):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    recipient = os.getenv("EMAIL_TO")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        subject = f"New message from {name}"
        body = f"From: {email}\n\n{message}"
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(sender, recipient, msg)

if __name__ == '__main__':
    app.run(debug=True)
