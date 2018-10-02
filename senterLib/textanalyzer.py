# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 01:34:06 2018

@author: Jedidiah & Timilehin
"""

import string
import random
import re
import pandas as pd

from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from os import listdir


class TextAnalyzer(object):

    """description of class"""

    def get_stopwords(self, address):
        with open(address, 'r') as stop:
            stopwords = stop.read().splitlines()
        return stopwords

    def __init__(self, id=random.randint(0, 4)):
        self.stopWords = self.get_stopwords("../Resources/stopwords.txt")
        self.MatrixCSV = "../Resources/OutData/WFMatrix" + str(id)
        self.negativeWords = self.get_stopwords("../Resources/negativeWords.txt")

    def read_csv(self, address, rowstostay, columnstotest, columnstodrop):
        data = pd.read_csv(address, encoding='ISO-8859-1')

        if(len(columnstodrop) > 0):
            data = data.drop(columnstodrop, axis=1)
        for col in columnstotest:
            data = data[data[col].map(rowstostay)]
        return data

    def __tweet_length(self, tweet):
        return [len(t) for t in tweet]

    def remove_usernames(self, tweet):
        return re.sub(r'@[A-Za-z0-9_]+', '', tweet)

    def removeHTMLTags(self, tweet):
        return BeautifulSoup(str(tweet), 'lxml').get_text()

    def removeURLs(self, tweet):
        return re.sub('https?://[a-zA-z0-9./]+', '', tweet)

    def lettersOnly(self, tweet):    # TODO remember to use this guy
        return re.sub("[^a-zA-z' ]", "", tweet)

    def removeMultipleLetters(self, tweet):
        newString = tweet[:2]
        i = 2
        while (i < len(tweet)):
            if(not (tweet[i] == tweet[i - 1] == tweet[i - 2])):
                newString += tweet[i]
        return newString

    def removeStopwords(self, collection):
        return [word for word in collection if word not in self.stopWords]

    def cleanTweets(self, data, tweetRow, nameOfNewTable):
        x = data[tweetRow]
        data[tweetRow] =[self.lettersOnly(self.remove_usernames(self.removeURLs(self.removeHTMLTags(t)))).strip().lower() for t in data[tweetRow]]
        data.to_csv(nameOfNewTable, sep=',', encoding='utf-8', index=False)

    def sanitize_text(self, text):
        text = text.strip()
        token = re.split('[ {0}]+'.format(string.punctuation).replace('@', ''),
                         text)

        if(token[-1] == ''):
            del token[-1]

        token = [t for t in token if not t.startswith("@")]  # Removes username

        # removes all the remaining @
        token = [word.lower() for word in token
                 if word not in self.stopWords + ["@"]]
        return token

    def stem_token(self, token):
        p = PorterStemmer()
        return [p.stem(t) for t in token]

    def CountTerms(self, folderPath, term):
        t = TextAnalyzer()
        cols = ['sentiment']
        data_dict = {}
        cols_to_drop = ['favoriteCount', 'created', 'truncated',
                        'id', 'screenName', 'retweetCount', 'isRetweet',
                        'longitude', 'latitude', 'location', 'language']
        for address in listdir(folderPath):
            data = t.read_csv(folderPath + "/" + address,
                              (lambda x: x > term),
                              cols, cols_to_drop)

            texts = data['text'].copy()
            all_txt = (' '.join(texts)).lower()
            all_txt = re.sub(r"[{0}]".format(string.punctuation), '', all_txt)
            all_txt = t.removeStopwords(all_txt.split())
            #all_txt = [word for word in all_txt if word in self.negativeWords]
            for txt in all_txt:
                if(txt in data_dict):
                    data_dict[txt] += 1
                else:
                    data_dict[txt] = 1

        data_dict_Freq = dict(sorted(data_dict.items(),
                                     key=lambda kvp: kvp[1], reverse=True))
        print(data_dict_Freq)
        return data_dict_Freq
    
    def cleanAllBanksTweets(self, folderpath, col_to_drop, cols_to_test,
                            row_to_stay, tweetRow, newFolderPath):
        t = TextAnalyzer()
        for bank in listdir(folderpath):
            data = t.read_csv(folderpath + "/" + bank, row_to_stay,
                              cols_to_test, col_to_drop)
            t.cleanTweets(data, tweetRow, newFolderPath + "/" + bank)


if __name__ == '__main__':

    t = TextAnalyzer()
    cols = ['text']

    folderPath = "../Resources/newClean"
    pda = t.CountTerms(folderPath, 0)
    d = {"[word]": list(pda.keys()), "[frequency]": list(pda.values())}
    df = pd.DataFrame(data=d)
    df.to_csv(t.MatrixCSV, sep=',', encoding='utf-8', index=False)
    
    
    #t.cleanAllBanksTweets(folderPath,[],["sentiment"], lambda x : x != 0, "",folderPath)
    #pda = t.CountTerms(folderPath, '1')
    #d = {"[word]": list(pda.keys()), "[frequency]": list(pda.values())}
    #df = pd.DataFrame(data=d)
    #df.to_csv("../Resources/OutData/PosVec", sep=',', encoding='utf-8', index=False)
    print("Done")
