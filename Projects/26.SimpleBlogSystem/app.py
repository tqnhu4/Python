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