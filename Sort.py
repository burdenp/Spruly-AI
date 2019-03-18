import sys
import os
import string
import Stock
import Count

#takes in a list of stocks and returns a sorted list of stocks
#sorts the list of stocks based on their weight value
#and stocks with weight 0 are culled
#list of stock -> list of stock
def sortStock(los):
	temp = sorted(los, key=lambda stock: stock.weight)
	for x in temp:
		if x.weight == 0:
			temp.remove(x)
	return temp