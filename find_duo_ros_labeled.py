import csv

with open('./dataset/informative_labeled_fr.csv', mode='w') as fri, open('./dataset/informative_labeled_p.csv', mode='w') as pi:
    writerfri = csv.writer(fri, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
    writerpi = csv.writer(pi, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(1, 6):
        print("Ckecking star "+str(i))
        with open('./dataset/raw_data_stars_'+str(i)+'.csv', 'rt') as f:
            reader = csv.reader(f)
            revs = list(reader)
        with open('./dataset/textblobed_training_'+str(i)+'.csv', 'rt') as f:
            reader = csv.reader(f)
            sents = list(reader)
        revs.pop(0)
        sents.pop(0)
        for rev in revs[1:]:
            if len(sents) == 0:
                break
            toPop = []
            for sent in sents:
                if sent[1] == '0':
                    toPop.append(sents.index(sent))
                if sent[1] == '1':
                    if sent[0].replace('"', '') in rev[3].replace('"', ''):
                        writerfri.writerow([rev[0]]+sent)
                    toPop.append(sents.index(sent))
                if sent[1] == '2':
                    if sent[0].replace('"', '') in rev[3].replace('"', ''):
                        writerpi.writerow([rev[0]]+sent)
                    toPop.append(sents.index(sent))
        for i in sorted(toPop, reverse=True):
            sents.pop(i)
