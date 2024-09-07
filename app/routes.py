from flask import render_template, redirect, url_for, request
from app import app

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Products page route (if you add one)
@app.route('/products')
def products():
    return render_template('products.html')

# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Example logic for handling login
        username = request.form.get('username')
        password = request.form.get('password')
        # Here you'd typically check the username and password with the database
        # For now, just redirect to the home page after login
        return redirect(url_for('index'))
    return render_template('login.html')

# Register page route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Example logic for handling registration
        username = request.form.get('username')
        password = request.form.get('password')
        # Here you'd typically save the new user to the database
        return redirect(url_for('login'))
    return render_template('register.html')