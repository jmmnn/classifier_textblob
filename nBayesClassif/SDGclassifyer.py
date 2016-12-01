#This is a single class text classifier example using a Naive Bayes algorithm. It is an adaptstion of the tutorial by http://textblob.readthedocs.io/

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ('I am poor.', 'poverty'),
    ('This society is in famine', 'hunger'),
    ('Hot weather is affecting the economy', 'climate'),
    ('This poor condition is lamentable.', 'poverty'),
    ("What hunger in this town", 'hunger'),
    ('I do not like this weather', 'climate'),
    ('I do not have money.', 'poverty'),
    ("The weather is so warm", 'climate'),
    ('The food was lacking', 'hunger'),
    ('My neighbor is poor.', 'poverty')
]
test = [
    ('The poor suffer from lack of money.', 'poverty'),
    ('Tha weather is getting hot', 'climate'),
    ("the lack of food is overwhelming.", 'hunger'),
    ("I don't have money", 'poverty'),
    ('Gary does not have any food', 'hunger'),
    ("Global climate weather change is happening.", 'climate')
]

cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify("Their weather is getting hot."))  # "climate"
print(cl.classify("I don't have food to eat."))   # "hunger"

# Classify a TextBlob
blob = TextBlob("The weather was increasing in temperature. There were people without food. "
                "My family did not have any money.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(5)
