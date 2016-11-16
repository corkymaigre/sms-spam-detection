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

1. split into tokens of alphabetic characters.
2. any space ( ), comma (,), dot (.), or any special characters are removed from feature space for now.
3. alphabetic strings are stored as a token as long as they do not have any non-alphabetic characters in between. 
4. the effect of abbreviations and misspellings in the messages are ignored.
5. no word stemming algorithm is used.
6. an additional token is generated with the number of dollar signs ($).
7. an additional token is generated with the number of numeric strings.
8. an additional token is generated with the overall number of character in the message.



