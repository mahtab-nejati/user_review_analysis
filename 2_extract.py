from bs4 import BeautifulSoup as bs
from langdetect import detect
from textblob import TextBlob
import csv

stars_1 = './dataset/raw_data_stars_1'
stars_2 = './dataset/raw_data_stars_2'
stars_3 = './dataset/raw_data_stars_3'
stars_4 = './dataset/raw_data_stars_4'
stars_5 = './dataset/raw_data_stars_5'

with open(stars_1+'.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["app", "ratings", "helpful-vote", "comment"])
with open(stars_2+'.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["app", "ratings", "helpful-vote", "comment"])
with open(stars_3+'.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["app", "ratings", "helpful-vote", "comment"])
with open(stars_4+'.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["app", "ratings", "helpful-vote", "comment"])
with open(stars_5+'.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["app", "ratings", "helpful-vote", "comment"])


apps = ['duolingo', 'rosettastone']

for appname in apps:

    section = bs(open('./dataset/source_'+appname+'.html'),
                 'html.parser').find('div', jsname='fk8dgd')
    reviews = section.findAll('div', class_='d15Mdf bAhLNe')
    print("\nThere are "+str(len(reviews)) +
          " reviews avaliable for "+appname.upper())
    print("Writing the data...")

    count = {'tots': 0, 'r1': 0, 'r2': 0, 'r3': 0, 'r4': 0, 'r5': 0}

    for review in reviews[:5000]:
        try:
            soup = review
            rating = soup.find('div', role='img').get(
                'aria-label').strip("Rated ")[0]
            helpful = soup.find(class_="jUL89d y92BAb").text
            if not helpful:
                helpful = 0
            comment = TextBlob(
                soup.find('span', jsname='fbQN7e').text.lower()).correct()
            if not comment:  # expand the comment button
                comment = TextBlob(
                    soup.find('span', jsname='bN97Pc').text.lower()).correct()
            comment = str(comment)
            if detect(comment) == 'en':
                if rating == '5':
                    with open(stars_5+'.csv', mode='a') as file:
                        writer = csv.writer(file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(
                            [appname, rating, helpful, comment])
                        count['tots'] += 1
                        count['r5'] += 1
                if rating == '4':
                    with open(stars_4+'.csv', mode='a') as file:
                        writer = csv.writer(file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(
                            [appname, rating, helpful, comment])
                        count['tots'] += 1
                        count['r4'] += 1
                if rating == '3':
                    with open(stars_3+'.csv', mode='a') as file:
                        writer = csv.writer(file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(
                            [appname, rating, helpful, comment])
                        count['tots'] += 1
                        count['r3'] += 1
                if rating == '2':
                    with open(stars_2+'.csv', mode='a') as file:
                        writer = csv.writer(file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(
                            [appname, rating, helpful, comment])
                        count['tots'] += 1
                        count['r2'] += 1
                if rating == '1':
                    with open(stars_1+'.csv', mode='a') as file:
                        writer = csv.writer(file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(
                            [appname, rating, helpful, comment])
                        count['tots'] += 1
                        count['r1'] += 1
        except:
            print("error")
    print(str(count['tots']) +
          ' English reviews found and saved for '+appname.upper()+'!')
    print('ONE STARS: ' + str(count['r1']))
    print('TWO STARS: '+str(count['r2']))
    print('THREE STARS: '+str(count['r3']))
    print('FOUR STARS: '+str(count['r4']))
    print('FIVE STARS: '+str(count['r5']))
