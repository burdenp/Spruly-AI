import sys
import os
import string
import Stock
import json

#takes in a json object returns a list of stocks
#takes in the json object from the site that corresponds
#to the stock info and converts it to a list of stock
#Json -> list of stocks
def farm(j):
     stocks = json.loads(j)
     temp = stocks['stock']
     #list of stocks returned
     final = []
     for s in temp:
     		#tempStock is the stock appeneded to final
            tempStock = stock(temp[name], temp[price],
            	temp[time], temp[views], temp[volume], temp[mcap], temp[pchange], temp[perchange])
            final.append(tempStock)
     return final



