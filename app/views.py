from flask import render_template
from flask import request
from app import app
import calculate

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_address = request.form['total']
    elif request.args.get('address'):
        user_address = request.args.get('address')
    else:
        user_address = "AJHsDRdyv5D62Btug5YQg598vqFTcGADqZ"
    return render_template("index.html",
    del_payments=calculate.del_payments(user_address),
    coin_balance=calculate.coin_balance(user_address),
    current_usd=calculate.get_usd(),
    total_received=calculate.total_received(user_address))
