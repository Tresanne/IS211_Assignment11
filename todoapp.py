#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""web app """


from flask import Flask,request,redirect
from flask import render_template

app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD=True
)

global todolist
todolist = []

@app.route('/')
def todolist_view():
	return render_template('index.html', todolist = todolist)

@app.route('/submit', methods=['POST'])
def submit_view():
	if request.form['task'] == '' or request.form['email'] == '' or request.form['priority'] == '':
		print 'no data'
	else:
		todoitem = {}
		todoitem['task'] = request.form['task']
		todoitem['email'] = request.form['email']
		todoitem['priority'] = request.form['priority']
		todolist.append(todoitem)
	return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_view():
	del todolist[:]
	return redirect('/')

if __name__ == '__main__':
	app.run()
