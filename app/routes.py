from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import SearchForm
from app.result import Result
import pandas as pd
import re

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# @app.route('/login', methods=('GET','POST'))
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect(url_for('index'))
#     return render_template('login.html', title='Sign In', form=form)

@app.route('/rimoj', methods=['GET','POST'])
def rimoj():
    if request.method == 'GET':
        query = request.args.get('r')
    else:
        query = request.form.get('query')
    results = []
    if query:
        df = pd.read_csv('./revo.csv', names=['link'], index_col=0)
        for i in range(len(query)-1):
            nomatch = query[:i]
            match = query[i:]
            if match == query:
                rule = match
            else:
                rule = '(?<!{nomatch}){match}'.format(nomatch=nomatch, match=match)
            filtered = df.filter(regex=re.compile('.*{rule}[aeiou]?$'.format(
                rule=rule), re.IGNORECASE), axis=0)
            if len(filtered) > 0 : # there were matches
                result = Result(matchString=match, 
                                words=filtered.index.to_list(),
                                links=filtered['link'].to_list())
                results.append(result)
    return render_template('rimoj.html', results=results, form=SearchForm(), title='Rimoj')