from textblob import TextBlob
import csv

for i in range(1, 6):

    with open('./dataset/labeled_training_sents_'+str(i)+'.csv', 'rt') as f:
        reader = csv.reader(f)
        sents = list(reader)

    with open('./test/processed_training_'+str(i)+'.csv', mode='w') as trifile:
        writer = csv.writer(trifile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        for row in sents:
            sent = row[0]
            sent = str(TextBlob(sent).correct())
            writer.writerow([sent, row[1]])
