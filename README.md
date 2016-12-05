# classifier
Basic generic text classifier using linear support vector machine (SVM) model.

Dependencies:
------------

- Ubuntu Server 16
- Miniconda (python)
- textblob


Install:
------------

Get installer script:  
  update link `$ wget https://raw.githubusercontent.com/jmmnn/classifier/master/server_installer.py`  

Run installer script, say yes when necessary:  
`$ python3 server_installer.py`  

Open a NEW TERMINAL  
`$ cd classifier_textblob`  

Crete new environment  
`$ python3 conda_setup.py`

Activate the new environemnt  
`$ source activate classifier`

#Install dependencies ### Not using this line for now
# $ pip install -r requirements.txt

Install textblob and download corpora
`$ pip install -U textblob`  
`$ python -m textblob.download_corpora`  

or
`python -m nltk.downloader gutenberg` # to get gutenberg corpus
`python -m nltk.downloader abc`

Run the classifier
`$ python SDGclassifyer.py`  ### TO DO ### : Add parameters indicating source files and destination

Afterwards load the Brown corpus

>>> from nltk.corpus import brown
brown.fileids()

head = brown.raw('ca01')

See some of it:
>>> len (brown.raw(categories='learned'))

Help on the functions to manipulate NLTK corpus go here: 
http://www.nltk.org/api/nltk.corpus.reader.html#corpus-reader-functions