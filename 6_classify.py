import csv
import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


with open('./dataset/classify_training_ni.csv', 'rt') as f:
    reader = csv.reader(f)
    training_ni = list(reader)

training_ni = np.array(training_ni).transpose()
training_ni_x = list(training_ni[:1, :][0, :])
training_ni_y = list(training_ni[1:, :][0, :])

cv_ni = CountVectorizer()
cv_training_ni_x = cv_ni.fit_transform(training_ni_x)

classifier_ni = MultinomialNB()
classifier_ni.fit(cv_training_ni_x, training_ni_y)

with open('./dataset/classify_training_i.csv', 'rt') as f:
    reader = csv.reader(f)
    training_i = list(reader)

training_i = np.array(training_i).transpose()
training_i_x = list(training_i[:1, :][0, :])
training_i_y = list(training_i[1:, :][0, :])

cv_i = CountVectorizer()
cv_training_i_x = cv_i.fit_transform(training_i_x)

classifier_i = MultinomialNB()
classifier_i.fit(cv_training_i_x, training_i_y)

results = {
    'duo': {
        'rated_1': {'ni': [], 'fri': [], 'pi': []},
        'rated_2': {'ni': [], 'fri': [], 'pi': []},
        'rated_3': {'ni': [], 'fri': [], 'pi': []},
        'rated_4': {'ni': [], 'fri': [], 'pi': []},
        'rated_5': {'ni': [], 'fri': [], 'pi': []}
    },
    'ros': {
        'rated_1': {'ni': [], 'fri': [], 'pi': []},
        'rated_2': {'ni': [], 'fri': [], 'pi': []},
        'rated_3': {'ni': [], 'fri': [], 'pi': []},
        'rated_4': {'ni': [], 'fri': [], 'pi': []},
        'rated_5': {'ni': [], 'fri': [], 'pi': []}
    }
}

for i in range(1, 6):
    with open('./dataset/sents_'+str(i)+'.csv', 'rt') as f:
        reader = csv.reader(f)
        sents = list(reader)
        for sent in sents[1:]:
            vect_ni = cv_ni.transform([sent[3]])
            prediction_ni = classifier_ni.predict(vect_ni)[0]
            if prediction_ni == '0':
                results[sent[0][0:3]]['rated_'+str(i)]['ni'].append(sent)
            if prediction_ni == '1':
                vect_i = cv_i.transform([sent[3]])
                prediction_i = classifier_i.predict(vect_i)[0]
                if prediction_i == '1':
                    results[sent[0][0:3]]['rated_'+str(i)]['fri'].append(sent)
                elif prediction_i == '2':
                    results[sent[0][0:3]]['rated_'+str(i)]['pi'].append(sent)

print("\n\nResults for Duolingo :")
for i in range(1, 6):
    print("")
    print("Rated "+str(i)+" star class NI :\t\t" +
          str(len(results['duo']['rated_'+str(i)]['ni'])))
    print("Rated "+str(i)+" star class FRI :\t" +
          str(len(results['duo']['rated_'+str(i)]['fri'])))
    print("Rated "+str(i)+" star class PI :\t\t" +
          str(len(results['duo']['rated_'+str(i)]['pi'])))

print("\n\nResults for Rosettastone :")
for i in range(1, 6):
    print("")
    print("Rated "+str(i)+" star class NI :\t\t" +
          str(len(results['ros']['rated_'+str(i)]['ni'])))
    print("Rated "+str(i)+" star class FRI :\t" +
          str(len(results['ros']['rated_'+str(i)]['fri'])))
    print("Rated "+str(i)+" star class PI :\t\t" +
          str(len(results['ros']['rated_'+str(i)]['pi'])))


with open('./dataset/informative_duo_fr.csv', mode='w') as dfri, open('./dataset/informative_duo_p.csv', mode='w') as dpi:
    writerfri = csv.writer(dfri, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
    writerpi = csv.writer(dpi, delimiter=',', quotechar='"',
                          quoting=csv.QUOTE_MINIMAL)
    duo = results['duo']
    for i in range(1, 6):
        rlist = duo['rated_'+str(i)]
        for sent in rlist['fri']:
            for i in range(int(sent[2])+1):
                writerfri.writerow(sent)
        for sent in rlist['pi']:
            for i in range(int(sent[2])+1):
                writerpi.writerow(sent)

with open('./dataset/informative_ros_fr.csv', mode='w') as rfri, open('./dataset/informative_ros_p.csv', mode='w') as rpi:
    writerfri = csv.writer(rfri, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
    writerpi = csv.writer(rpi, delimiter=',', quotechar='"',
                          quoting=csv.QUOTE_MINIMAL)
    ros = results['ros']
    for i in range(1, 6):
        rlist = ros['rated_'+str(i)]
        for sent in rlist['fri']:
            # for i in range(int(sent[2])+1):
            writerfri.writerow(sent)
        for sent in rlist['pi']:
            # for i in range(int(sent[2])+1):
            writerpi.writerow(sent)
