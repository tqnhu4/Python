from .forms import ContactForm
from flask import Blueprint, Flask, redirect, render_template, url_for, request, flash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/projects')
def projects():
    projects_data = [
        {'title': 'Project A', 'description': 'Description for Project A', 'link': 'https://github.com/user/projectA'},
        {'title': 'Project B', 'description': 'Description for Project B', 'link': None},
        # Add more projects here
    ]
    return render_template('projects.html', projects=projects_data)    

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Xử lý dữ liệu form hoặc gửi email
        flash("Message sent!", "success")
        return redirect(url_for('main.contact'))
    return render_template('contact.html', form=form)

