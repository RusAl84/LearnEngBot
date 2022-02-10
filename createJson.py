import json
qutesList=[]
quoteItem1={}
quoteItem1['text']="Возьмёмся за руки друзья. Возьмёмся за руки друзья. Чтоб не пропасть поодиночке."
quoteItem1['trans']="Let’s join hands friends. Let’s join hands friends. In order not to perish one by one."
quoteItem1['author']="Булат Окуджава"
qutesList.append(quoteItem1)
quoteItem2={}
quoteItem2['text']="Пока Земля ещё вертится, пока ещё ярок свет, Господи, дай же ты каждому, чего у него нет: мудрому дай голову, трусливому дай коня, дай счастливому денег… И не забудь про меня."
quoteItem2['trans']=""
quoteItem2['author']="Булат Окуджава"
qutesList.append(quoteItem2)

jsonString = json.dumps(qutesList, ensure_ascii=False)
jsonFile = open("data.json", "w", encoding="UTF-8")
jsonFile.write(jsonString)
jsonFile.close()