import polowrapper
import requests
import json

#response = requests.Request('https://poloniex.com/public?command=returnTicker')
#response = requests.post('https://poloniex.com/public?command=returnTicker')
#output = json.loads(response.text)['BTC_XMR']['percentChange']
#output = json.loads(response.read())
#print (output)


a = polowrapper.poloniex('L70DN1US-G4620JC9-WNGMCD2Z-E7P8PF21','869be3f3947af0ee9e8e6a6ad152dc81c174587df73968150765560d3dffb1179db95bf98098167aef4512290a53724f594a0a71fc81493e63b7e6ec909d3fcf')
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

