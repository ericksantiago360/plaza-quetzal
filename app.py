from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/coworking')
def coworking():
    return render_template('coworking.html')

@app.route('/gastronomia')
def gastronomia():
    return render_template('gastronomia.html')

@app.route('/artesanias')
def artesanias():
    return render_template('artesanias.html')

if __name__ == '__main__':
    app.run(debug=True) 