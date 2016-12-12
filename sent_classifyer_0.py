
#Generic classifier
'''
Allows you to train a classifier to detect 1 specific topic, 
then feed an unclassified corpus of documents
it will return 
    - Each sentence in the new documents will be classified ( yes / no ) if it is about the topic. 
      Saved to yml or json file (also indicating the name of the parent document).
    - (optionnally) a classification for the entire document (yes / no)

Steps:
- Training corpus: Get 10 long documents in text format (.txt) specialized in the domain you wish to identify, 
  save them in a known directory.

- Analyzed corpus: Place the documents you wish to analyze in text format (.txt) in known directory

- Configure the variables:

Variables:
---------
train_Corpus_Path =     #default to localpath
analyze_Corpus_Path =   #default to localpath
category_label =        #enter the label you want to assign e.g. science, technology, etc.
random_Corpus_Path =    #provided by default, you don't need to change it, but you can.

'''

import nltk
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

# helper function to load a text corpus
def assignCorpus (path):
    newCorpus = nltk.corpus.PlaintextCorpusReader(path, '.*\.txt')
    return newCorpus

#Run function above to load each corpus (train, analyzed, random)

def sampleFromCorpora (setName, sources):
    '''
    #[
    [corpus, fileid, label , numSents = 5, startSent = 0],
    [etc. for each set of samples to add]
    ]'''
    setName = []
    for item in sources:
        corpus = assignCorpus(item[0])
        for sent in corpus.sents(item[1])[item[4]:item[4]+item[3]]:
            setName.append((' '.join(sent) , item[2]))
    print (setName)

    # ['sdgs', 'wess2009.txt', 'tata' , 2, 0] ,
 


# Generic function to take data from a corpus and prepare it for textBlob
# def sampleFromCorpora (corpus, label, fileids = ' ', numSents = 10, startSent = 0):
#     '''numSents is the number of sentences to use, use startSent to avoid begining sentences'''
#     test = []
#     for sent in corpus.sents(fileids)[startSent:startSent+numSents]:
#         test.append((' '.join(sent) , label))
#     return test

#train = sampleFromCorpus()

#run it three times to build the train, analyzed and random sets

# function to train the model
def trainModel (algorithm, trainingSet):
    pass

# buid a test set, combining some random sentences from the trining set and the random set

# Function to compute accuracy
#def getAccuracy(model, testSet):
    #print("Accuracy: {0}".format(cl.accuracy(test)))

#helper function to save all sentences from a document analyzed to a json file
#def saveResultsToFile (sentence, sourceFile, tag, resultsFile):

# Function to run model on the new corpus
#def classifier (model, targetCorpus)

