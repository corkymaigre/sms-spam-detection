import string
from collections import Counter
from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer

def getNumberOfUppercaseWords(_list):
    "This calculate the number of words in uppercase in the message"
    n = 0
    for elem in _list:
        l = len(elem) #length of the token
        u = sum(c.isupper() for c in elem) #number of character in uppercase       
        if u==l: #if all characters are in uppercase
            n+=1
    return n

with open('../output/data.arff', 'w') as out:
    out.write('@relation sms\n')
    out.write('\n@attribute ncharacter real\n')
    out.write('@attribute ndollars real\n')
    out.write('@attribute nnumeric real\n')
    out.write('@attribute nuppercase real\n')
    out.write('@attribute type {ham, spam}\n')
    out.write('\n@data\n')

try:
    stemmer = SnowballStemmer("english")
    file = open('../dataset/SMSSpamCollection', 'r')
    for line in file: 
        counter = Counter(line) #create a counter 
        number_of_character = len(line) #number of character in the message
        number_of_dollars = counter['$'] #number of dollars in the message            
        number_of_numeric = sum(c.isdigit() for c in line) #number of numeric value in the message
        line = line.translate(str.maketrans('.,;:/?!@#$&~#{([|-_^)]+=}*%', '                           ')) #remove special characters        
        tokens = line.split() #split the message into words
        number_of_uppercase_word = getNumberOfUppercaseWords(tokens) #number of words in uppercase in the message        
        tokens = [stemmer.stem(token.lower()) for token in tokens] #convert all tokens into lowercase and find the word root
        tokens.insert(0,number_of_character) #insert the number of character at 1st place
        tokens.insert(1,number_of_dollars) #insert the number of dollars at 2nd place
        tokens.insert(2,number_of_numeric) #insert the number of numerical value at 3rd place
        tokens.insert(3,number_of_uppercase_word) #insert the number of words in uppercase at 4th place
        
        #print(tokens)
        
        with open('../output/data.arff', 'a') as out:
            i = 0
            for token in tokens[:5]:
                i+=1
                if i!=5:
                    out.write(str(token) + ',')
                else:
                    out.write(str(token) + '\n')
                
        
        
except Exception as e:
    print('Error: ' + str(e))



