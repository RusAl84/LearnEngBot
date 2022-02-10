import nltk
import pymorphy2


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

if __name__ == '__main__':
    nltk.download('stopwords')
    nltk.download('punkt')
    str1="Две вещи наполняют разум всё возрастающим удивлением и трепетом, чем чаще и интенсивнее к ним обращается ум мысли: звёздное небо надо мной и моральный закон внутри меня."
    mas=getKeywords(str1)
    print(mas)

