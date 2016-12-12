#tester
import sent_classifyer_0 as classy

#test function assignCorpus
# corpusSDG = classy.assignCorpus('sdgs')
# print (corpusSDG.fileids())

# [corpus, fileid, label , numSents = 5, startSent = 0],
fuentes = [ 
    ['sdgs', 'wess2009.txt', 'tata' , 2, 0] ,
    ['malapata', 'wess2010.txt' , 'gena' , 2 , 0 ]
            ]    
classy.sampleFromCorpora ('train', fuentes)