import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('login.html')

@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    return render_template('home.html') 

@app.route('/submit_details', methods=['GET', 'POST']) 
def submit_details(): 
    return redirect(url_for('index')) 

@app.route('/contacts', methods=['GET']) 
def contacts(): 
    contacts = "" 
    return render_template('contacts.html', contacts=contacts) 

if __name__ == '__main__':
   app.run()
