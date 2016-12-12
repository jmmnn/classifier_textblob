#This is a single class text classifier example using a Naive Bayes algorithm. It is an adaptation of the tutorial by http://textblob.readthedocs.io/

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from nltk.corpus import gutenberg
from nltk.corpus import abc as corpus

# lenght = len (corpus.raw())
# print (corpus.readme())
#print (gutenberg.fileids())
#print (corpus.fileids())
#head = corpus.raw('science.txt')
train = []
for sent in corpus.sents('science.txt')[50:150]:
    train.append((' '.join(sent) , 'science'))
for sent in gutenberg.sents('austen-emma.txt')[50:150]:
    train.append((' '.join(sent) , 'austen'))
for sent in gutenberg.sents('shakespeare-hamlet.txt')[5:150]:
    train.append((' '.join(sent) , 'shakes'))
for sent in gutenberg.sents('melville-moby_dick.txt')[5:150]:
    train.append((' '.join(sent) , 'melville'))    
    #print ("new_____" , ' '.join(sent))
#print (train2)
# # print (corpus.words('science.txt'))

test = []
for sent in corpus.sents('science.txt')[400:420]:
    test.append((' '.join(sent) , 'science'))
for sent in gutenberg.sents('austen-emma.txt')[400:420]:
    test.append((' '.join(sent) , 'austen'))
for sent in gutenberg.sents('shakespeare-hamlet.txt')[400:420]:
    test.append((' '.join(sent) , 'shakes'))
for sent in gutenberg.sents('melville-moby_dick.txt')[400:420]:
    test.append((' '.join(sent) , 'melville'))
cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify("Mar. What, ha's this thing appear'd againe to night"))  # "shakes"
print(cl.classify("Where now it burnes, Marcellus and my selfe"))   # "shakes"

print(cl.classify("Emma Woodhouse, handsome, clever, and rich, with a comfortable home"))  # "austen"
print(cl.classify("Sixteen years had Miss Taylor been in Mr. Woodhouse's family"))   # "austen"

print(cl.classify("We travelled almost 3 billion miles in space. We visited a comet, grabbed a piece of it and it landed here this morning, Brownlee said an incredible thrill"))  # "science"
print(cl.classify("It was twinkling a little bit, getting a little brighter, and moving. I thought, maybe that's a helicopter. But it kept getting brighter and brighter and brighter"))   # "science"

print(cl.classify("Gotcha! A colourful, striking image can spark your interest"))  # "science"
print(cl.classify("Australian associate professor of psychology Bill von Hippel"))   # "science"

print(cl.classify("long-pampered Gabriel, Michael, and Raphael, against your coming"))  # "melville"
print(cl.classify("Leviathan maketh a path to shine after him; One would think the deep to be hoary"))   # "melville"

# # Classify a TextBlob
# blob = TextBlob("The poor weather was increasing in temperature. There were people without food. "
#                 "My family did not have any money, they were very poor.", classifier=cl)
 
# print(blob.classify())

# for sentence in blob.sentences:
#     print(sentence)
#     print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(25)
