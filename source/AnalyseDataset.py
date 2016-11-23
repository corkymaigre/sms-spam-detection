import string

from collections import Counter




try:
	file = open('../dataset/SMSSpamCollection', 'r')
	for line in file: 
                counter = Counter(line)  
                number_of_character = len(line)
                number_of_dollars = counter['$']                
                number_of_numeric = sum(c.isdigit() for c in line)
                line = line.translate(None, '.,;:/?!@#$&~#{([|-_^)]+=}*%')
                tokens = line.split()
                tokens.insert(0,number_of_character)
                tokens.insert(1,number_of_dollars)
                tokens.insert(2,number_of_numeric)
		print(tokens)
		#break
except: pass