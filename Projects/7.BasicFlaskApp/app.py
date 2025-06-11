from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lưu tạm tên đã gửi
user_names = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            user_names.append(name)
            return redirect(url_for('greet', username=name))
    return render_template('form.html')

@app.route('/greet/<username>')
def greet(username):
    return render_template('greet.html', username=username, all_users=user_names)

if __name__ == '__main__':
    app.run(debug=True)
