from arky import api
from arky.util import stats
import urllib, json

def del_payments():
    api.use("ark")
    #print api.Account.getAccount("AUahWfkfr5J4tYakugRbfow7RWVTK35GPW")
    history = stats.getHistory("AJHsDRdyv5D62Btug5YQg598vqFTcGADqZ")
    del_payment = []
    for transaction in history:
        if transaction["senderId"] == "AUexKjGtgsSpVzPLs6jNMM6vJ6znEVTQWK":
            transaction["senderId"] == str(transaction["senderId"])
            transaction["senderId"] = transaction["senderId"][0:15]
            transaction["amount"] = float(transaction["amount"] / 100000000)
            del_payment.append(transaction)
    return del_payment

def total_received():
    api.use("ark")
    history = stats.getHistory("AJHsDRdyv5D62Btug5YQg598vqFTcGADqZ")
    total = 0.0
    for transaction in history:
        if transaction["senderId"] == "AUexKjGtgsSpVzPLs6jNMM6vJ6znEVTQWK":
            total = total + transaction["amount"]
    return float(total / 100000000)

def get_usd():
    url = "https://api.coinmarketcap.com/v1/ticker/ark/"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return float(data[0]["price_usd"])

def coin_balance():
    interest_rate = 0.00010958904 # 0.04 / 365
    usd_value = get_usd()
    balance = stats.getBalanceHistory("AJHsDRdyv5D62Btug5YQg598vqFTcGADqZ")
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
