import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from random import randint
import csv

wordnet_lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
punctuations = "?:!.,;\"'"
count = {'training': 0, 'testing': 0}

fileNames = ['training', 'training_ni', 'training_i',
             'testing', 'testing_ni', 'testing_i']

english_vocab = set(w.lower() for w in nltk.corpus.words.words())


for name in fileNames:
    with open('./dataset/classify_'+name+'.csv', 'rt') as f:
        reader = csv.reader(f)
        sents = list(reader)

    with open('./dataset/repreprocessed_'+name+'.csv', mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)

        for sent in sents:
            words = word_tokenize(sent[0])
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
            writer.writerow([' '.join(words)]+[sent[1]])
