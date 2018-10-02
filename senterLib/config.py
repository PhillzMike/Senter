# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 23:57:49 2018

@author: Jedidiah & Timilehin
"""
import pandas as pd

from naivebayes import NaiveBayes
from os import listdir


class input(object):

    @staticmethod
    def divideData(trainingData):
        testData = list()
        testLabel = list()
        trainingD = list()
        trainingLabel = list()
        for i in range(trainingData.shape[0]):
            #print(str(trainingData[i][1]).strip())
            if(i%1000 == 0):
                testData.append((str(trainingData.iloc[i,0]).strip()))
                testLabel.append(str(trainingData.iloc[i,1]).strip())
            else:
                trainingD.append(str(trainingData.iloc[i,0]).strip())
                trainingLabel.append(str(trainingData.iloc[i,1]).strip())

        return (trainingD,trainingLabel, testData,testLabel)

    @staticmethod
    def extract(address, textPosition, sentimentPosition):
        data = pd.read_csv(address, encoding='ISO-8859-1')
        return input.divideData(data.iloc[:, [textPosition, sentimentPosition]])

    @staticmethod
    def writeTo(address,bayes):

        data = pd.read_csv(address, encoding='ISO-8859-1')
        ans = list()
        for i in range(data.shape[0]):
            ans.append(bayes.classify(data.iloc[i,0]))
        data["sentiment"] = ans;
        data.to_csv(address, sep=',', encoding='utf-8', index=False)

    @staticmethod
    def percent_negative_tweets(address):
        data = pd.read_csv(address, encoding= 'ISO-8859-1')
        negative_tweets = 0
        for sentiment in data["sentiment"]:
            if(sentiment == 0):
                negative_tweets += 1

        return float(negative_tweets)/len(data["sentiment"] * 100)

    def DoToAll(folderPath, method, parameters = None):
        for bank in listdir(folderPath):
            if(parameters == None):
                print(method(folderPath + "/" + bank))
            else:
                print(method(folderPath + "/" + bank, parameters))

(trainingData, trainingSentiment, testData, testSentiment) = input.extract("../Resources/SentimentAnalysisDataset.csv", 2, 1)
(td, ts, ted, tes) = input.extract("../Resources/SenterTrainingData.csv", 5, 0)
ts = ["0" if t == "0" else "1" for t in ts ]
tes = ["0" if t == "0" else "1" for t in tes ]
print(ts)
print("good")
print(tes)

testData += ted
testSentiment += tes
bayes = NaiveBayes()
bayes.train(trainingData,trainingSentiment, ["0", "1"])
correct = 0

#for i in range(len(testData)):
#    ans = bayes.classify(testData[i])
    #if(ans == (testSentiment[i] == "1")):
#    if(ans == testSentiment[i]):
#        correct += 1
#print(float(correct)/len(testData) * 100)
input.DoToAll("../Resources/CleanTables",input.writeTo,parameters = bayes)
print("Done")
input.DoToAll("../Resources/CleanTables",input.percent_negative_tweets)
#print(input.percent_negative_tweets("cleanTable/Accessbank.csv"))
#print(input.percent_negative_tweets("cleanTable/DiamondBank.csv"))
#print(input.percent_negative_tweets("cleanTable/EcoBank.csv"))
#print(input.percent_negative_tweets("cleanTable/FCMB.csv"))
#print(input.percent_negative_tweets("cleanTable/gtbank.csv"))
#print(input.percent_negative_tweets("cleanTable/Skyebank.csv"))
#print(input.percent_negative_tweets("cleanTable/UBA.csv"))
#print(input.percent_negative_tweets("cleanTable/Wema.csv"))
#print(input.percent_negative_tweets("cleanTable/zenith.csv"))
#print(input.percent_negative_tweets("cleanTable/Fidelity.csv"))
print("Done")


