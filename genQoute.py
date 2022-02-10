import json
from getKeywords import getKeywords 
import random

def genQoute(str1):
    fileObject = open("data3.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    keywords1=getKeywords(str1)
    print(keywords1)
    nList=[]
    cSet=set()
    for item in aList:
        countIntersections=0
        keywords2=item['keywords']
        for i1 in keywords1:
            for i2 in keywords2:
                if i1==i2:
                    countIntersections+=1
        item['countIntersections']=countIntersections
        nList.append(item)
        cSet.add(countIntersections)
    ciMax=max(list(cSet))
    qList=[]
    for item in nList:
        if item['countIntersections']==ciMax:
            qList.append(item)
            # print(item['text'])
    # return qList
    str2=qList[random.randrange(len(qList))]['text']
    return str2
    # print(qList)


if __name__ == '__main__':
    str1="Сколько веревочки не длится"
    # str1="теоретическая и практическая значимость работы  конкретика в постановке цели и задач  "
    str2 =genQoute(str1)
    print(str2)


