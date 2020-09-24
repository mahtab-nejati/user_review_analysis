import csv
from nltk import sent_tokenize
from random import randint

count = {'r1': 0, 'r2': 0, 'r3': 0, 'r4': 0, 'r5': 0, 'tots': 0,
         't1': 0, 't2': 0, 't3': 0, 't4': 0, 't5': 0, 'ttots': 0}

for i in range(1, 6):

    with open('./dataset/raw_data_stars_'+str(i)+'.csv', 'rt') as f:
        reader = csv.reader(f)
        revs = list(reader)

    with open('./dataset/sents_'+str(i)+'.csv', mode='w') as dfile, open('./dataset/training_sents_'+str(i)+'.csv', mode='w') as tfile:
        writerd = csv.writer(dfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_MINIMAL)
        writert = csv.writer(tfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_MINIMAL)
        writerd.writerow(["app", "ratings", "helpful-vote", "sentence"])
        for rev in revs[1:]:
            sents = sent_tokenize(rev[3])
            for sent in sents:
                writerd.writerow([rev[0], rev[1], rev[2], sent])
                count['r'+str(i)] += 1
                count['tots'] += 1
            # flag = randint(1, 10) < 9
            # if not flag:
            #     for sent in sents:
            #         writert.writerow([sent, ''])
            #         count['t'+str(i)] += 1
            #         count['ttots'] += 1


print("\nTotal number of sentences: "+str(count['tots']))
for i in range(1, 6):
    print('\tWITH RATING '+str(i)+' : '+str(count['r'+str(i)]))
print('Trainingset (total of '+str(count['ttots'])+'):')
for i in range(1, 6):
    print('\tWITH RATING '+str(i)+' : '+str(count['t'+str(i)]))
