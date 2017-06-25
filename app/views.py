from flask import render_template
from app import app
import calculate

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", del_payments=calculate.del_payments(), \
    coin_balance=calculate.coin_balance(),
    current_usd=calculate.get_usd(),
    total_received=calculate.total_received())
