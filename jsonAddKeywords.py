import nltk
import pymorphy2
nltk.download('stopwords')
nltk.download('punkt')

def getKeywords(str1):
    mas=[]
    morph = pymorphy2.MorphAnalyzer()
    for i in str1.split():
        if len(i)>3:
            p = morph.parse(i)[0]
            mas.append(p.normal_form)
    set2 = set()
    for item in mas:
        if not "nan" in str(item).replace(" nan ", " "):
            set2.add(str(item).replace(" nan ", " "))
    mas = list(set2)
    mas.sort()
    return(mas)

import json

fileObject = open("data2.json", "r", encoding="UTF-8")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)

nList=[]
for item in aList:
    str1=item['text']
    # str1="Две вещи наполняют разум всё возрастающим удивлением и трепетом, чем чаще и интенсивнее к ним обращается ум мысли: звёздное небо надо мной и моральный закон внутри меня."
    keywords=getKeywords(str1)
    # print(keywords)
    item['keywords'] = keywords
    nList.append(item)

jsonString = json.dumps(nList, ensure_ascii=False)
jsonFile = open("data3.json", "w", encoding="UTF-8")
jsonFile.write(jsonString)
jsonFile.close()