from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import SearchForm
from app.result import Result
import pandas as pd
import re

# TODO: Add an arrow next to each that allows for searching by that word

@app.route('/', methods=['GET','POST'])
def index():
    query = request.form.get('query')
    radikoj = request.form.get('radikoj')
    vokalo = request.form.get('vokalo')
    results = []
    if query:
        # clean the query
        query = "".join(re.split("[^a-zA-ZĉŝĥĵĝŭĈŜĤĴĜŬ.]*", query)) # only letters from query
        if vokalo and (query[-1] in 'aeiou'):
            query  = query[:-1]

        # load and prepare the file of roots or words
        filepath = './revo_radikoj_git.csv' if radikoj else './revo_vortoj_git.csv'
        ending = '' if radikoj else '[aeiou]?' # if looking for all words, look for all vowel endings
        df = pd.read_csv(filepath, names=['link'], index_col=0)

        # find all matches
        for i in range(min(len(query),20)):
            match = query[i:] # match only on the terminal slice of the word
            # skip when there are no more vowels
            if not re.match('^.*[aeiou].*$', match):
                break
            nomatch = query[i-1:i] # don't match if the letter before the match string matches
            rule = match if match == query else '(?<!{nomatch}){match}'.format(nomatch=nomatch, match=match)
            filtered = df.filter(regex=re.compile('.*{rule}{ending}$'.format(
                rule=rule, ending=ending), re.IGNORECASE), axis=0)
            if len(filtered) > 0 : # there were matches
                result = Result(matchString=match, 
                                words=filtered.index.to_list(),
                                links=filtered['link'].to_list())
                results.append(result)

    return render_template('index.html', results=results, form=SearchForm(), method=request.method)

@app.route('/pri')
def pri():
    return render_template('pri.html')

@app.route('/sxangxlisto')
def sxangxlisto():
    return render_template('sxangxlisto.html')