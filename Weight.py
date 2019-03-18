import sys
import os
import string
import Stock
import Count

#assigns weight to a given list of stocks
#List of stocks && Dict -> List of stocks
def weightStock(los, count):
	for i in range(len(los)):
		los[i].weight = algo(los[i], count[los[i].name])







#WORK ON ALGO
#Stocks that are fed in have to use 
#their provided info from the api
# and the count from another program
#algo is thhe weight assigning algorithm
#takes a stock and a count returns a weight
#stock & num -> num
def algo(stock, count):
	#rough code being put in here
	#rough formula is
	#name + views + price + volume +market cap + price change + percent change
	#0 + (stock.views * modifier) + stock.price + (stock.volume * mod) + 
	#(stock.mcap * mod) + (stock.pchange * mod) + (stock.perchange * mod)
	# + (mod * count)
	return 0 + (stock.views * 1) + stock.price + (stock.volume * 100) + \
	     (stock.mcap * 5) + (stock.pchange * 5) + (stock.perchange * 1000)
