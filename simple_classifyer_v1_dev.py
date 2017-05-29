
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
'''
# Configuration:
# ---------
train_Corpus_Path = 'cybersecurity'    #default to localpath
test_Corpus_Path = 'cybersecurity_test'    #default to localpath
analyze_Corpus_Path = 'target_Corpus'  #default to localpath
category_label = 'cybersecurity'       #enter the label you want to assign e.g. science, technology, etc.
random_Corpus_Path = 'randomText'      #provided by default, you don't need to change it, but you can.
################
import nltk
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

#Use this function to create your Training Corpus, Test Corpus e.g.:
# training = createCorpora(training_sources)
def createCorpus (path , label):
    newSet = []
    corpus = nltk.corpus.PlaintextCorpusReader(path, '.*\.txt')
    for sent in corpus.sents():
        newSet.append((' '.join(sent) , label))
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
    corpus = nltk.corpus.PlaintextCorpusReader(path, '.*\.txt')
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

### Create corpora
training_Corpus = createCorpus(train_Corpus_Path , category_label)
test_Corpus = createCorpus(test_Corpus_Path , category_label)
random_Corpus = createCorpus(random_Corpus_Path , 'random')
#target_Corpus = createCorpus(analyze_Corpus_Path, 'unknown')

### Crate and train a model
classifier = NaiveBayesClassifier(training_Corpus)
#
#Test accuracy using the testing Corpus
#print("Accuracy: {0}".format(classifier.accuracy(random_Corpus)))

### Run the classifier on the target corpus
classifyCorpus (classifier, 'target_Corpus')

#helper function to save all sentences from a document analyzed to a json file
#def saveResultsToFile (sentence, sourceFile, tag, resultsFile):
