from flask import render_template
from flask import request
from app import app
import calculate

@app.route('/')
@app.route('/index')
def index():
    user_address = request.args.get('address')
    return render_template("index.html",
    del_payments=calculate.del_payments(user_address),
    coin_balance=calculate.coin_balance(user_address),
    current_usd=calculate.get_usd(),
    total_received=calculate.total_received(user_address))
