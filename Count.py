import sys
import os
import string
import Stock
import collections
#purpose is to count the given stocks and figure out how many
#there are of each stock and then pass that onto format/weight

#takes in a list of stocks, returns a dictionary
#takes in the list of stocks and then finds the names
#then compares names to the dictionary and if they are already in it
#increase the count by one
#list of stocks -> dictionary
#dictionary is in the format
#{StockName : count}
def count(l):
	total = dict
	for key in l:
		if key in total:
			total.key =+ 11
        else:
        	total.key = 1
	return total