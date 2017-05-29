
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

# helper function to load a text corpus to NLTK format
def assignCorpus (path):
    newCorpus = nltk.corpus.PlaintextCorpusReader(path, '.*\.txt')
    return newCorpus

#Use this function to create your Training Corpus, Test Corpus, and Target Corpus, e.g.:
# training = createCorpora(training_sources)
def createCorpora (sources):
    ''' sources is a list of corpora in this format:
    [
        [corpusFolder, filename.txt, label , numSents = 5, startSent = 0],   # example: ['sdgs', 'wess2009.txt', 'tata' , 2, 0] ,
        [etc. for each set of samples to add]
    ]
    '''
    newSet = []
    for item in sources:
        corpus = assignCorpus(item[0])
        for sent in corpus.sents(item[1])[item[4]:item[4]+item[3]]:
            newSet.append((' '.join(sent) , item[2]))
    #print (newSet)
    return newSet

# helper function write to file function
def writteToFile(filename, extension, content):
    '''example: writteToFile('helloWorld' , '.txt' , 'Hello World')
    '''
    with open(filename + extension, 'w') as f:
        f.write(content)

def classifyCorpus (model, path, toFile = 'yes' , onScreen = 'no'):
    ''' Main function to classify the sentences of a corpus of documents
    '''
    corpus = assignCorpus(path)
    contentToFile = []
    for sent in corpus.sents() :
        textChunk = ( model.classify(sent) , ' : ' , str(sent))
        # if onScreen == 'yes':
        #     print(textChunk)
        #     pass
        if toFile == 'yes':
            contentToFile.append(textChunk)
    writteToFile('result' , '.txt' , str(contentToFile))
    return contentToFile

#List the sources for a corpus
training_sources = [
            ['cybersecurity', 'legal.txt', 'legal' , 10, 0],
            ['cybersecurity', 'organizational.txt', 'organizational' , 10, 0],
            ['cybersecurity', 'technical.txt', 'technical' , 10, 0],
            ['randomText', 'random.txt', 'random' , 10, 0],
            ]

test_sources = [
            ['cybersecurity', 'legal.txt', 'legal' , 5, 11],
            ['cybersecurity', 'organizational.txt', 'organizational' , 5, 11],
            ['cybersecurity', 'technical.txt', 'technical' , 5, 11],
            ['randomText', 'random.txt', 'random' , 5, 11]
            ]

target_sources = [
            ['target_Corpus', 'Afghanistan.txt', 'unknown' , 10, 10]
            ]

### Create corpora
training_Corpus = createCorpora(training_sources)
test_Corpus = createCorpora(test_sources)
#target_Corpus = createCorpora(target_sources)

### Crate and train a model
classifier = NaiveBayesClassifier(training_Corpus)

#Test accuracy using the testing Corpus
#print("Accuracy: {0}".format(classifier.accuracy(test_Corpus)))

### Run the classifier on the target corpus
classifyCorpus (classifier, 'target_Corpus')

#helper function to save all sentences from a document analyzed to a json file
#def saveResultsToFile (sentence, sourceFile, tag, resultsFile):
