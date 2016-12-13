#tester
#import sent_classifyer_0 as classy
from sent_classifyer_0 import *

#test function assignCorpus
# corpusSDG = classy.assignCorpus('sdgs')
# print (corpusSDG.fileids())

# [corpus, fileid, label , numSents = 5, startSent = 0],
trainSet = [ 
    ['sdgs', 'wess2009.txt', '2009' , 10, 0] ,
    ['malapata', 'wess2010.txt' , '2010' , 10 , 0 ]
          ]    
train = createCorpora (trainSet)     #e.g. to create a training set

testSet = [ 
    ['sdgs', 'wess2009.txt', '2009' , 10, 120] ,
    ['malapata', 'wess2010.txt' , '2010' , 10 , 120 ]
    ]

test = createCorpora (testSet)     #e.g. to create a training set

# train
mymodel = NaiveBayesClassifier(train)

# Compute accuracy
print("Accuracy: " , mymodel.accuracy(test))

# Classify target corpus
classifyCorpus (mymodel, 'smt')