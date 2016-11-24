from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
def index():
    user = {'nickname': 'Vasantha Ganesh Kanniappan'}
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/p', methods=['GET', 'POST'])
def prob():
    problem = {'id':101,
               'pname':'watermelons',
               'statement':'Once upon a time there was a crow',
               'blk': [{'id':1, 'tcase':'hello eon', 'ssoln':'mellow'},
                       {'id':2, 'tcase':'jam bingo', 'ssoln':'vangaugh'}]}
    return render_template('prob.html',
                           title=problem["id"],
                           problem=problem)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="{}", remember_me={}'.format(form.openid.data,
                                                                       str(form.remember_me.data)))
        return redirect('/')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/u')
def userprofile():
    profile = {'name':'Vasantha Ganesh Kanniappan',
               'desc': 'Lambda guru, Free Software Enthusiast and amateur competitive programmer',
               'attempted': 250,
               'solved': 205}
    return render_template('userprofile.html',
                           title = "About {}".format(profile['name']),
                           profile=profile)
    
