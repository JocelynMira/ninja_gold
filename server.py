from flask import Flask, session, render_template, redirect, request
from random import randint
from datetime import datetime

app = Flask (__name__)
app.secret_key = 'gold_is_life'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['moves'] = 0
        session['activities'] = []
    return render_template ('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
    location = request.form['location']
    if location == 'farm':
        add_gold = randint(10,20)
    elif location == 'cave':
        add_gold = randint(5,10)
    elif location == 'house':
        add_gold = randint(2,5)
    else:
        add_gold = randint(-50, 50)
    session['gold'] += add_gold
    session['moves'] += 1
    if add_gold > 0:
        linecolor = 'green'
    else:
        linecolor = 'red'
    session['activities'].insert( 0,{'Activity': f" <p style='color: {linecolor}'> Earned {add_gold} gold from the {location}. {datetime.now()} </p> "})
    print(add_gold)
    return redirect('/')
    #insert instead of append will insert item at a given position so we start index at index 0.


@app.route('/reset_game')
def reset_game():
    session.clear()
    return redirect ('/')

if __name__ == '__main__':
    app.run(debug=True)