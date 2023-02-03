from flask import Flask, session, render_template, redirect, request
from random import randint


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
        session['moves'] += 1
        session['gold'] += add_gold
        session['activities'].append({'message': f"You got {session['gold']}."})
    print(add_gold)
    return redirect ('/')

@app.route('/reset_game')
def reset_game():
    session.clear()
    return redirect ('/')


if __name__ == '__main__':
    app.run(debug=True)