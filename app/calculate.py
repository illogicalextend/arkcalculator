from arky import api
from arky.util import stats
from decimal import Decimal
from collections import Counter
import urllib, json

def get_delegates():
    api.use("ark")
    delegate = api.Delegate()
    delegates = delegate.getDelegates()
    return delegates['delegates']

def top_delegate(del_payments):
    c = Counter()
    for transaction in del_payments:
        c[transaction["del_username"]] += 1
    return c.most_common()[0][0]

def del_payments(user_address):
    api.use("ark")
    history = stats.getHistory(user_address)
    del_payments = []
    delegates_list = get_delegates()
    total_received = 0.0
    for transaction in history:
        for delegate in delegates_list:
            if transaction["senderId"] == delegate['address']:
                transaction["senderId"] == str(transaction["senderId"])
                transaction["senderId"] = transaction["senderId"][0:8]
                transaction["amount"] = float(Decimal(transaction["amount"]) / 100000000)
                transaction["fee"] = float(Decimal(transaction["fee"]) / 100000000)
                transaction["del_username"] = delegate['username']
                total_received = total_received + transaction["amount"]
                del_payments.append(transaction)
                break
    #top_delegate(del_payments)
    return {'del_payments':del_payments, 'total_received':total_received, 'top_delegate':top_delegate(del_payments)}

def get_usd():
    url = "https://api.coinmarketcap.com/v1/ticker/ark/"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return float(data[0]["price_usd"])

def coin_balance(user_address):
    interest_rate = 0.00010958904 # 0.04 / 365
    usd_value = get_usd()
    balance = stats.getBalanceHistory(user_address)
    balance = balance[-1][1]
    estimates = {}
    estimates['balance'] = balance
    estimates["1day"] = (1 * balance * interest_rate)
    estimates["1week"] = (7 * balance * interest_rate)
    estimates["1month"] = (30 * balance * interest_rate)
    estimates["1year"] = (365 * balance * interest_rate)
    estimates["1dayusd"] = (1 * balance * interest_rate * usd_value)
    estimates["1weekusd"] = (7 * balance * interest_rate *usd_value)
    estimates["1monthusd"] = (30 * balance * interest_rate * usd_value)
    estimates["1yearusd"] = (365 * balance * interest_rate * usd_value)
    return estimates
