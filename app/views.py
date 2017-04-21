from flask import render_template
from app import app
from datetime import datetime

@app.route('/')
@app.route('/index')

def index():
	user = {'nickname' : 'Pippo'}
	posts = [
		{
			'author' : {'nickname' : 'John'},
			'body' : 'Beautiful day in Portland!',
			'date' : str(datetime.now().day) + '-' + str(datetime.now().month)
		},
		{	
			'author' : {'nickname' : 'Jim'},
			'body' : 'This is a second post',
			'date' : str(datetime.now().day) + '-' + str(datetime.now().month)
		}
			]
		
	return render_template('index.html',title='Home',user=user,posts=posts)
