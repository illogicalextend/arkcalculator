# -*- encoding: utf8 -*-
# © Toons

import sys, imp, json, requests, traceback
# from .. import setInterval

class ExchangeNoImplemented(Exception): pass
class ExchangeApiError(Exception): pass

def main_is_frozen():
	return (hasattr(sys, "frozen") or hasattr(sys, "importers") or imp.is_frozen("__main__"))

class Exchange:

	frozen_mode = False

	@staticmethod
	def _printError(error):
		if hasattr(error, "__traceback__"):
			sys.stdout.write("".join(traceback.format_tb(error.__traceback__)).rstrip() + "\n")
		sys.stdout.write("%s\n" % error)

	@staticmethod
	def coinmarketcap(curency):
		try:
			cmc_ark = json.loads(requests.get("http://coinmarketcap.northpole.ro/api/v5/ARK.json").text)
			return float(cmc_ark["price"][curency])
		except Exception as error:
			Exchange._printError(error)

	@staticmethod
	def cryptocompare(curency):
		try:
			if Exchange.frozen_mode:
				ccp_ark = json.loads(requests.get("https://min-api.cryptocompare.com/data/price?fsym=ARK&tsyms=USD,EUR,GBP,CNY", verify='cacert.pem').text)
			else:
				ccp_ark = json.loads(requests.get("https://min-api.cryptocompare.com/data/price?fsym=ARK&tsyms=USD,EUR,GBP,CNY").text)
			return float(ccp_ark[curency.upper()])
		except Exception as error:
			Exchange._printError(error)

def useExchange(name):
	Exchange.frozen_mode = main_is_frozen()
	global getArkPrice
	try: getArkPrice = getattr(Exchange, name)
	except: raise ExchangeNoImplemented("%s exchange not implemented yet" % name.capitalize())
	else: return name.capitalize()

useExchange("coinmarketcap")
















# def getKrakenPair(pair):
# 	data = json.loads(requests.get("https://api.kraken.com/0/public/Ticker?pair="+pair.upper()).text)
# 	A, B = pair[:3], pair[3:]
# 	A = ("Z" if A in ['USD', 'EUR', 'CAD', 'GPB', 'JPY'] else "X") + A
# 	B = ("Z" if B in ['USD', 'EUR', 'CAD', 'GPB', 'JPY'] else "X") + B
# 	try: return float(data["result"][A + B]["c"][0])
# 	except: return -1


# def getPoloniexPair(pair):
# 	if "_" not in pair: pair = pair[:3] + "_" + pair[3:]
# 	return float(poloniex_json[pair]["last"])

# # poloniex global data 
# # reload data every 30 seconds
# @setInterval(60) 
# def load():
# 	global poloniex_json
# 	poloniex_json = json.loads(requests.get("https://poloniex.com/public?command=returnTicker").text)
# # load()
