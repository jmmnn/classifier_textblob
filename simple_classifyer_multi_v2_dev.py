
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

# helper function to load a text corpus to NLTK format. Default takes all .txt files in given path
def assignCorpus (path, files = '.*\.txt'):
    newCorpus = nltk.corpus.PlaintextCorpusReader(path, files)
    return newCorpus
#longCorpus = assignCorpus ('cybersecurity')    ####test lines
# print (longCorpus.fileids())
# legalCorpus = assignCorpus ('cybersecurity' , 'legal.txt')
# print (legalCorpus.fileids())
# print (len(longCorpus.sents()))
# print (len(longCorpus.sents('technical.txt')))

#Use this function to create your Training Corpus, Test Corpus, and Target Corpus, e.g.:
# training = createCorpora(training_sources)
def createCorpora (sources , stage='dev'):
    ''' sources is a list of corpora in this format:
    [
        [corpusFolder, filename.txt, label, startSent, numSents],   # example: ['sdgs', 'wess2009.txt', 'sdgs' , 0, 2] ,
        [etc. for each set of samples to add]
    ]
    Use stage = 'prod' to use all the training text.
    '''
    newSet = []
    # for item in sources:
    #     corpus = assignCorpus(item[0])
    #     for sent in corpus.sents(item[1])[item[3]:item[3]+item[4]]:
    #         newSet.append((' '.join(sent) , item[2]))
    # return newSet
    for item in sources:
        corpus = assignCorpus(item[0])
        if stage=='dev':
            for sent in corpus.sents(item[1])[item[3]:item[3]+item[4]]:
                newSet.append((' '.join(sent) , item[2]))
        else:
            for sent in corpus.sents(item[1]):
                newSet.append((' '.join(sent) , item[2]))
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
    labels = model.labels()
    for sent in corpus.sents():
        distribution = model.prob_classify(sent)
        scores = [round(distribution.prob(label) , 2) for label in labels]
        tags = dict(zip(labels , scores)) #dict(zip()) makes a dictionary from two lists
        textChunk = dict(zip(['tags' , 'sentence'] , ( tags ,  sent)))
        # textChunk = ( model.classify(sent) , ' : ' , str(sent))
        # if onScreen == 'yes':
        #     print(textChunk)
        #     pass
        if toFile == 'yes':
            contentToFile.append(textChunk)
    writteToFile('result' , '.txt' , str(contentToFile))
    return contentToFile

#List the sources for a corpus
training_sources = [
            ['cybersecurity', 'legal.txt', 'legal' , 0, 10],
            ['cybersecurity', 'organizational.txt', 'organizational' , 0, 10],
            ['cybersecurity', 'technical.txt', 'technical' , 0, 10],
            ['randomText', 'random.txt', 'random' , 0, 10],
            ]

test_sources = [
            ['cybersecurity', 'legal.txt', 'legal' , 15, 2],
            ['cybersecurity', 'organizational.txt', 'organizational' , 15, 2],
            ['cybersecurity', 'technical.txt', 'technical' , 15, 2],
            ['randomText', 'random.txt', 'random' , 15, 2]
            ]

### Create corpora
dev_training_Corpus = createCorpora(training_sources)
test_Corpus = createCorpora(test_sources)
prod_training_Corpus = createCorpora(training_sources , 'prod')

### Crate and train a model
#classifier = NaiveBayesClassifier(dev_training_Corpus)
classifier = NaiveBayesClassifier(prod_training_Corpus)

# #Test accuracy using the testing Corpus
print("Accuracy: {0}".format(classifier.accuracy(test_Corpus)))

### Run the classifier on the target corpus
classifyCorpus (classifier, 'target_Corpus')

#helper function to save all sentences from a document analyzed to a json file
#def saveResultsToFile (sentenceUniqueId, sentence, sourceFile, tags, resultsFile):
