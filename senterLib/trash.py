## -*- coding: utf-8 -*-
#"""
#Created on Sun Sep 16 13:05:07 2018
#
#@author: Koudu
#"""
#
#
##        import re
##
##        brokenWords = []
##        sentenceList = []
##
##        delimiters = Formalizer.__regex(delimiters)
##        sentenceList = re.split(delimiters, word)
##        if sentenceList[-1] == ' ':
##            del sentenceList[-1]
##        for item in sentenceList:
##            Formalizer.breakme(item, brokenWords)
##        return brokenWords
#    @staticmethod
#    def breakme(word, brokenWords):
#
#        if("'" in word and len(word) != 1):
#            _set = sorted(set(word), key=word.index)
#            newWord = ""
#            for item in _set:
#                if(item == "'"):
#                    newWord += "'"
#                else:
#                    newWord += item
#            word = newWord
#            Formalizer.__check(word, brokenWords)
#
#        else:
#            brokenWords.append(word)
#
#    @staticmethod
#    def __regex(delims):
#        if(delims[0] == '[' and delims[-1] == ']'):
#            return delims
#        else:
#            return '[' + delims + ']'
#
#    @staticmethod
#    def __check(word, brokenWords):
#
#        fword = ""
#        sword = ""
#
#        if(word[0] != "'"):
#            # if no, it checks for the different possible ending letters
#                if(word[-1] == 'a'):
#                    if(word[-2] == 'n' and word[-3] == 'n' and word[0] == 'g'):
#                        brokenWords.append("going")
#                        brokenWords.append("got")
#                    brokenWords.append("to")
#
#                elif (word[0] == 'd'):
#                    fword = word.split("'")[0]
#                    sword = "ha" + word.split("'")[1]
#                    brokenWords.append(fword)
#                    brokenWords.append(sword)
#
#                elif(word[0] == 'e'):
#                    fword = word.split("'")[0]
#                    _t = word.split("'")[1]
#
#                    if(_t == "ve"):
#                        sword = "have"
#                    elif(_t == "re"):
#                        sword = "are"
#                    brokenWords.append(fword)
#                    brokenWords.append(sword)
#
#                elif(word[0] == "l"):
#                    _t = word.split("'")
#                    if(_t[0] == 'y'):
#                        fword = _t[0] + "ou"
#                    else:
#                        fword = _t[0]
#
#                    sword = "wi" + _t[1]
#                    brokenWords.append(fword)
#                    brokenWords.append(sword)
#
#                elif(word[0] == 's'):
#                    _t = word.split("'")
#                    fword = _t[0]
#                    sword = 'i' + _t[1]
#                    brokenWords.append(fword)
#                    brokenWords.append(sword)
#
#                elif(word[0] == 't'):
#                    _t = word.split("'")
#                    fakeText = _t[0]
#                    fword = fakeText[:-1]
#                    sword = "no" + _t[1]
#                    brokenWords.append(fword)
#                    brokenWords.append(sword)
#
#                else:
#                    _t = word.split("'")
#                    fword = _t[0]
#                    sword = 'i' + _t[1]
#                    brokenWords.append(fword)
#
## END