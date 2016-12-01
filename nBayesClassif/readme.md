## This is a simple naive Bayes Classifier
Using the textblob python package. more about textblob here: https://textblob.readthedocs.io/en/latest/

In the case of text classification it is often useful to use multiclass classification. 
However this example for simplicity only assigns one class to each sentence being classified.

#Install dependencies
 $ sudo pip install -r requirements.txt
 
# Afterwards download corpus for text training
$ python -m textblob.download_corpora

#Finally, run the classification example and view the results on screen.
$ python SDGclassifyer.py
