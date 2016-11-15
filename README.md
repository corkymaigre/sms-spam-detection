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

Each line of dataset is formated as follow:
* label of the message
* text message string

### Algorithms

The established email filtering algorithms are not efficient for SMS since:
* short length
* informal language
* full of abbreviations


The extraction and analysis of the data is done with Python.

The machine learning algorithms tested are:
* naive Bayes
* SVM
* ...


