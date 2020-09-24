import csv
import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

fileNames = ['', '_ni', '_i']

for name in fileNames:
    with open('./dataset/repreprocessed_training'+name+'.csv', 'rt') as f:
        reader = csv.reader(f)
        training = list(reader)

    with open('./dataset/repreprocessed_testing'+name+'.csv', 'rt') as f:
        reader = csv.reader(f)
        testing = list(reader)

    training = np.array(training).transpose()
    training_x = list(training[:1, :][0, :])
    training_y = list(training[1:, :][0, :])

    testing = np.array(testing).transpose()
    testing_x = list(testing[:1, :][0, :])
    testing_y = list(testing[1:, :][0, :])

    cv = CountVectorizer()
    cv_training_x = cv.fit_transform(training_x)

    classifier = MultinomialNB()
    classifier.fit(cv_training_x, training_y)

    cv_testing_x = cv.transform(testing_x)
    predictions = classifier.predict(cv_testing_x)

    results = classification_report(testing_y, predictions)

    if name == '':
        print('\nResults for classifying all sentences into 3 classes at once :')
    elif name == '_ni':
        print('\nResults for classifying all sentences into 2 classes of "Informative" and "Non-Informative" :')
    elif name == '_i':
        print('\nResults for classifying informative senctences into 2 classes of "Praising" and "Feature-Requesting" :')
    print(results)
