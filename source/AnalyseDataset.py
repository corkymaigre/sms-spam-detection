import os
import re

try:
	dataset_file = open('../dataset/SMSSpamCollection.txt', 'rb')
	for line in dataset_file:
		print(line)
except: pass
os.system('pause')