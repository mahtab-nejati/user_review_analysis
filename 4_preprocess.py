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

english_vocab = set(w.lower() for w in nltk.corpus.words.words())

for i in range(3):

    with open('./dataset/training_cat_'+str(i)+'.csv', 'rt') as f:
        reader = csv.reader(f)
        sents = list(reader)

    with open('./dataset/processed_training_cat_'+str(i)+'.csv', mode='w') as training, open('./dataset/processed_testing_cat_'+str(i)+'.csv', mode='w') as testing:
        writertr = csv.writer(training, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)
        writerte = csv.writer(testing, delimiter=',', quotechar='"',
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
            if randint(1, 10) < 9:
                writertr.writerow([' '.join(words)])
                count['training'] += 1
            else:
                writerte.writerow([' '.join(words)])
                count['testing'] += 1

print("\nTotal number of labeled sentences: " +
      str(count["training"]+count["testing"]))
print("\tTraining: "+str(count["training"]))
print("\tTesting: "+str(count["testing"]))
