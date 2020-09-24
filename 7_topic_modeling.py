import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from random import randint
import csv
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from gensim import matutils, models
import scipy.sparse

wordnet_lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
punctuations = "?:!.,;\"'"

files = ['informative_ros_p']

english_vocab = set(w.lower() for w in nltk.corpus.words.words())

for name in files:

    all_data = []
    with open('./dataset/'+name+'.csv', 'rt') as f:
        reader = csv.reader(f)
        sents = list(reader)

        for sent in sents:
            words = word_tokenize(sent[3])
            filtered = [word for word in words if not word in stop_words]
            filtered = [word for word in filtered if not word in punctuations]
            words = []
            for word in filtered:
                words.append(wordnet_lemmatizer.lemmatize(word, pos="v"))
            filtered = words[:]
            words = []
            for word in filtered:
                words.append(wordnet_lemmatizer.lemmatize(word, pos="n"))
            filtered = words[:]
            words = []
            for word in filtered:
                words.append(wordnet_lemmatizer.lemmatize(word, pos="a"))
            filtered = words[:]
            words = []
            for word in filtered:
                if word in english_vocab:
                    words.append(word)
            all_data.append(' '.join(words))

    cv = CountVectorizer()
    vector = cv.fit_transform(all_data)
    transposed = vector.transpose()
    sparse_counts = scipy.sparse.csr_matrix(np.array(transposed).any())
    corpus = matutils.Sparse2Corpus(sparse_counts)
    id2word = dict((v, k) for k, v in cv.vocabulary_.items())
    lda = models.LdaModel(corpus=corpus, id2word=id2word,
                          num_topics=5, passes=10)
    topics = lda.print_topics()
    for topic in topics:
        print(topic)
