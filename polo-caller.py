import polowrapper
import requests
import json

#response = requests.Request('https://poloniex.com/public?command=returnTicker')
#response = requests.post('https://poloniex.com/public?command=returnTicker')
#output = json.loads(response.text)['BTC_XMR']['percentChange']
#output = json.loads(response.read())
#print (output)


a = polowrapper.poloniex('','')
#a.returnTicker()
#test = a.returnMarketTradeHistory('BTC_XMR')
#print (json.dumps(test, indent=4, sort_keys=True))

retTicker = a.returnTicker()
print ("BTC/XMR Prize: " + retTicker['BTC_XMR']['last'] + " BTC")
print ("24H High Prize: " + retTicker['BTC_XMR']['last'] + " BTC")
retBalance = a.returnBalances()
print ("Current Balance: " + retBalance['XMR'] + " XMR")
print ("Open Orders:")
openOrders = a.returnOpenOrders('BTC_XMR')
print (openOrders)
#print ("Trade History:")
#tradeHistory = a.returnTradeHistory('BTC_XMR')
#print (json.dumps(tradeHistory, indent=4, sort_keys=True))

