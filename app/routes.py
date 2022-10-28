from turtle import title
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    # return "Hello World"
    user_info = {'name': 'Dung'}
    number_list = ['one', 'two', 'three']
    students_info = [{'name': 'Hi', 'java': '8', 'php': '7', 'c': '9'},
                     {'name': 'ha', 'java': '8', 'php': '7', 'c': '9'},
                     {'name': 'hu', 'java': '8', 'php': '7', 'c': '9'},
                     ]

    return render_template('index.html', user=user_info, title="Home Page", list=number_list, students=students_info)


@app.route('/signin')
def login_form():
    return render_template('signin.html')
