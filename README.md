# sms-spam-ml
## SMS Spam Detection using Machine Learning Approach


### Motivation

Short Message Service (SMS) is a text communication platform that allows mobile phone users
to exchange short text messages (usually less than 160 7-bit characters) at a low cost.
The amount of unsolicited commercial advertisements (spams) over SMS will be bigger since
the cost of SMS will decrease.

SMS spam is not familiar compared to mail spam.

### Datasets

The dataset for this project is a large text file established by a database of 5574 real text
messages from UCI Machine Learning repository gathered in 2012 which contains:
* 425 SMS spam messages from the Grumbletext website (a UK forum in which cell phone users make public claims about SMS spam.
* 3375 SMS non-spam messages from the NUS SMS Corpus (NSC).
* 450 SMS non-spam messages from Caroline Tag's PhD Thesis.
* 1002 SMS non-spam and 322 spam messages from SMS Spam Corpus v.0.1 Big.

Downloaded from [SMS Spam Collection Data Set from UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection).


Each line of dataset is formatted as follow:
* label of the message
* text message string

### Algorithms

The established email filtering algorithms are not efficient for SMS since:
* short length
* informal language
* full of abbreviations


The extraction and analysis of the data is done with Python.

The machine learning algorithms tested are:
* Naive Bayes Algorithm
* Support Vector Machine (SVM) Algorithm
* k-Nearest Neighbor Algorithm
* ...


#### Data Extraction

For each text message:

1. count the overall number of characters.
2. count the number of dollars.
3. count the number of numeric characters.
4. count the number of words in uppercase.
5. remove space ( ), comma (,), dot (.), or any special characters.
6. convert all words into lowercase.
7. split into tokens of alphabetic characters.
8. add a token at the begining with the number of characters.
9. add a token at the 2nd place with the number of dollars.
10. add a token at the 3rd place with the number of numeric characters.
11. add a token at the 4th place with the number of words in uppercase.

There are some problems with very special characters, need to fix that.

It might be great to seek the root of a word (e.g., walk, walks, walked, walking have the root 'walk' in common).
See NLTK for more information.



#### Machine Learning Algorithms

An association algorithm can be established to distinguish two sets: a ham set and a spam set.
