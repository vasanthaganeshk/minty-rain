from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Vasantha Ganesh Kanniappan'}
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/prob')
def prob():
    problem = {'id':101,
               'pname':'watermelons',
               'statement':'Once upon a time there was a crow',
               'blk': [{'id':1, 'tcase':'hello eon', 'ssoln':'mellow'},
                       {'id':2, 'tcase':'jam bingo', 'ssoln':'vangaugh'}]}
    return render_template('prob.html',
                           problem=problem)
