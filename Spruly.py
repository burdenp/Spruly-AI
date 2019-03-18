import sys
import os
import string
import Stock
import Count
import Farm
import Sort
import Weight


#Run this file
#this file still needs to have the ability
#to be fed JSON objects from an external source

def main(j):
     stocks = Farm.farm(j)
     sortStocks = Weight.weightStock(stocks, Count.count(stocks))
     sortedStocks = sort.sortStock(sortedStocks)
     print sortedStocks
     return sortedStocks

JSON = sys.argv[1]

print main(JSON)