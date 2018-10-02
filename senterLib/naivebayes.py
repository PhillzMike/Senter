# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 13:53:34 2018

@author: f
"""

from formalizer import Formalizer
import math
from textanalyzer import TextAnalyzer
import operator
class NaiveBayes(object):
    def __init__(self):
        self.trainingData = dict()
        self.contractor = Formalizer()
        
    def train(self,trainingData, trainingSentiment, classes):
        if(len(classes) < 2):
            raise ValueError("Number of classes in the training data should be greater than 1")
        self.probabilityOfClasses = {str(x) : 0 for x in classes}
        self.classes = [x for x in classes]
        classesDict = {str(x) : dict() for x in classes}
        allWords = set()
        count = 0
        self.analyzer = TextAnalyzer()
        for tData in trainingData:
            if(tData == ""):
                continue
            words = list()
            data = self.analyzer.sanitize_text(tData)
            for word in data:
                words.extend(self.analyzer.stem_token([x for x in self.contractor.expand(word)]))

            classDict = classesDict[trainingSentiment[count]]

            self.probabilityOfClasses[trainingSentiment[count]] += 1
            for word in words:
                if(word == ""):
                    continue
                if(word in classDict):
                    classDict[word] += 1
                else:
                    classDict[word] = 1
                allWords.add(word)
            count += 1
            if(count % 100000 == 0):
                print(count)

        probDict = {x: dict() for x in classesDict}
        for word in allWords:
            wordSentiment = [0 for x in classes]
            totalWordCount = 0
            for i, classDict, prob in zip(range(len(classesDict)), classesDict.values(), probDict.values()):
                if word in classDict:
                    wordSentiment[i] = classDict[word]
                    totalWordCount += wordSentiment[i]
                    prob[word] = 0
            for i, classDict in zip(range(len(probDict)), probDict.values()):
                if word in classDict:
                    classDict[word] = float(wordSentiment[i])/totalWordCount
        self.trainingData = probDict

        for n in self.probabilityOfClasses:
            self.probabilityOfClasses[n] /= len(trainingData)



    def classify(self,sentence):
        words = list()
        sentence = self.analyzer.sanitize_text(sentence)
        for word in sentence:
            words.extend(self.analyzer.stem_token([x for x in self.contractor.expand(word)]))

        probabilityOfClasses = {x : self.probabilityOfClasses[x] for x in self.probabilityOfClasses}
        for word in words:
            word = word.lower()
            for clas in self.trainingData:
                if word in self.trainingData[clas]:
                    probabilityOfClasses[clas] += math.log(self.trainingData[clas][word])

        return max(probabilityOfClasses.items(), key = operator.itemgetter(1))[0]


    





