Sure, here is a sample Python code for some of the tasks. I'll use Flask and SQLAlchemy for this example.

```python
# Import necessary libraries
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(username=request.form['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['username'] = user.username
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = User.query.filter_by(username=session['username']).first()
    tasks = Task.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', tasks=tasks)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

This is a basic implementation and does not include form validation, error handling, UI design, testing, deployment, and maintenance. Those would require additional code and tools. Also, the HTML templates 'register.html', 'login.html', and 'dashboard.html' need to be created in a 'templates' folder.

Please note that this is just a simple demonstration of how to implement these features, and the actual implementation may vary based on the specific requirements of your project.