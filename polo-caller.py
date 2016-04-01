import polowrapper
import requests
import json

a = polowrapper.poloniex('','')

retTicker = a.returnTicker()
print ("BTC/XMR Prize: " + retTicker['BTC_XMR']['last'] + " BTC")
print ("24H High Prize: " + retTicker['BTC_XMR']['last'] + " BTC")
retBalance = a.returnBalances()
print ("Current Balance: " + retBalance['XMR'] + " XMR")
print ("Open Orders:")
openOrders = a.returnOpenOrders('BTC_XMR')
print (openOrders)
