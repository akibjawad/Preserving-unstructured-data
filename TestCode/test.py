import spacy as sp
import pandas as pd 

x = sp.__version__

from anonymization import *


def oneLineAnonymization(text: str) -> str:
    anon = AnonymizerChain(Anonymization('en_US'))
    anon.add_anonymizers(EmailAnonymizer, NamedEntitiesAnonymizer("en_core_web_sm"))
    anonText = anon.anonymize(text)
    return anonText

dataFrame = pd.read_csv('bbc.csv', encoding="utf-16", delimiter=',')
dataFrame = dataFrame.set_index("id", drop=False)
dataFrame = dataFrame.loc[:,"message"]
print('Read messages and started anonymizing')

output=open('anonymizedMessages.txt','w')
dataLength = dataFrame.__len__()
previousProgress = 0
# text = "Hi John,\nthanks for you for subscribing to Superprogram, feel free to ask me any question at secret.mail@Superprogram.com \n Superprogram the best program!"
for i in range(dataLength):
    # print('index ',i,' ',dataFrame[i])
    if pd.isnull(dataFrame[i]):
        continue
    anontext = oneLineAnonymization(dataFrame[i])
    output.write('index: '+str(i)+ ' '+anontext+'\n\n')
    currentProgress = (i/float(dataLength))*100
    if previousProgress != int(currentProgress):
        print("Progress is::"+ str(currentProgress)+"%")
        previousProgress = int(currentProgress) 
    # print(anontext)
output.close()
print("Generated anonymized text in format index:Anonymized text")