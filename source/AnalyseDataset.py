import string
from collections import Counter
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

def getNumberOfUppercaseWords(_list):
    "This calculate the number of words in uppercase in the message"
    n = 0
    for elem in _list:
        l = len(elem) #length of the token
        u = sum(c.isupper() for c in elem) #number of character in uppercase       
        if u==l: #if all characters are in uppercase
            n+=1
    return n

try:
    lmtzr = WordNetLemmatizer()
    file = open('../dataset/SMSSpamCollection', 'r')
    for line in file: 
        counter = Counter(line) #create a counter 
        number_of_character = len(line) #number of character in the message
        number_of_dollars = counter['$'] #number of dollars in the message            
        number_of_numeric = sum(c.isdigit() for c in line) #number of numeric value in the message
        line = line.translate(None, '.,;:/?!@#$&~#{([|-_^)]+=}*%') #remove special characters
        tokens = line.split() #split the message into words
        number_of_uppercase_word = getNumberOfUppercaseWords(tokens) #number of words in uppercase in the message        
        tokens = [token.lower() for token in tokens] #convert all toekns into lowercase.
        tokens.insert(0,number_of_character) #insert the number of character at 1st place
        tokens.insert(1,number_of_dollars) #insert the number of dollars at 2nd place
        tokens.insert(2,number_of_numeric) #insert the number of numerical value at 3rd place
        tokens.insert(3,number_of_uppercase_word) #insert the number of words in uppercase at 4th place
        
        print(lmtzr.lemmatize('cars'))
        #print(tokens)
except Exception, e:
    print('Error: ' + str(e))



