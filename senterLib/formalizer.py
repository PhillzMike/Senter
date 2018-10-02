# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 01:33:34 2018

@author: Jedidiah & Timilehin
"""


class Formalizer(object):

    """description of class"""

    def __init__(self):
        self.contracts = self.getContracts("../Resources/contracts.txt")

    def getContracts(self, address):
        with open(address, 'r') as contract:
            contracts = contract.read().splitlines()
        cnt = [line.split('-') for line in contracts]
        cnt0 = dict([(lc[0], lc[1].split(',')[0]) for lc in cnt])
        return cnt0

    def expand(self, word, delimiters="\t\n "):

        if word in self.contracts:
            return self.contracts[word].split()
        else:
            return word.split()
