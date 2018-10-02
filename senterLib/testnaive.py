from textblob import TextBlob
from os import listdir
import pandas as pd
import re


def writeTo(address):

    data = pd.read_csv(address, encoding='ISO-8859-1')
    ans = list()
    for i in range(data.shape[0]):
        ans.append(TextBlob(data.iloc[i,0]).sentiment.polarity)
    data["sentiment"] = ans;
    data.to_csv(re.sub('CleanTables','newClean',address), sep=',', encoding='utf-8', index=False)

def DoToAll(folderPath, method):
        for bank in listdir(folderPath):
            method(folderPath + "/" + bank)
            print("Done with", bank)
                
#DoToAll("../Resources/CleanTables",writeTo)

s = TextBlob("Transaction not working well, failed, I'm upset, atm, bank")
print(s.tags)