#This is a single class text classifier example using a Naive Bayes algorithm. It is an adaptation of the tutorial by http://textblob.readthedocs.io/

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

#poverty trainer

train = [
    ('I am poor.', 'y'),
    ('This society is in famine and poor', 'y'),
    ('Hot weather is affecting the poor economy', 'y'),
    ('This poor condition is lamentable.', 'y'),
    ("What hunger in this poor town", 'y'),
    ('I do not like this poor weather', 'y'),
    ('I do have money.', 'y'),
    ("The weather is so warm", 'n'),
    ('The food was lacking', 'n'),
    ('My neighbor is rich.', 'n')
]
test = [
    ('The poor suffer from lack of money.', 'y'),
    ('Tha weather is getting hot', 'n'),
    ("the lack of food is overwhelming.", 'n'),
    ("I don't have money", 'y'),
    ('Gary does not have any food', 'n'),
    ("Global climate weather change is happening.", 'n')
]

cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify("Their village was so poor"))  # "y"
#print(cl.classify("I have my sandals"))   # "n"
print ('labels : ' , cl.labels())

#See the probability of each label
prob_dist = cl.prob_classify("Their village was so poor")
print (prob_dist.max())  #the higherst probability
print(prob_dist.prob("n")) #probability of no
print(prob_dist.prob("y")) #probability of yes

# Classify a TextBlob
# blob = TextBlob("The poor weather was increasing in temperature. There were people without food. "
#                 "My family did not have any money, they were very poor.", classifier=cl)
# print(blob)
# print(blob.classify())
#
# for sentence in blob.sentences:
#     print(sentence)
#     print(sentence.classify())

# Compute accuracy
#print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
#cl.show_informative_features(5)
