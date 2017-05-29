#This is a single class text classifier example using a Naive Bayes algorithm. It is an adaptation of the tutorial by http://textblob.readthedocs.io/
import nltk
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
#from nltk.corpus import wess
from nltk.corpus import gutenberg

# lenght = len (corpus.raw())
# print (corpus.readme())
#print (wess.fileids())
#print (gutenberg.fileids())


##### Creating a new corpus
wess_dir = nltk.data.find('corpora/wess')
print (wess_dir)

my_wess = nltk.corpus.PlaintextCorpusReader(wess_dir, '.*\.txt')
print (my_wess.sents())
