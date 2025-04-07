import csv, random, math

fakeDict = dict()
trueDict = dict()

with open('data/Fake.csv', 'r', encoding="utf8") as file:
    text=csv.reader(file)
    for row in text:
        words = row[1].split()
        for i in words:
            i = i.strip().lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(";", "").replace("'", "").replace('"', "")
            if i not in fakeDict:
                fakeDict[i] = 1
            else:
                fakeDict[i] += 1
            if "total_cnt" not in fakeDict:
                fakeDict["total_cnt"] =1
            else:
                fakeDict["total_cnt"] +=1
     
with open('data/True.csv', 'r', encoding="utf8") as file:
    text=csv.reader(file)
    for row in text:
        words = row[1].split()
        for i in words:
            i = i.strip().lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(";", "").replace("'", "").replace('"', "").replace('(', "").replace(')', "").replace('[', "").replace(']', "").replace('{', "").replace('}', "").replace(',', "").replace('.', "").replace('-', "").replace('_', "")
            if i not in trueDict:
                trueDict[i] = 1
            else:
                trueDict[i] += 1
            if "total_cnt" not in trueDict:
                trueDict["total_cnt"] =1
            else:
                trueDict["total_cnt"] +=1

def randomWords(num):
    ret = []
    for i in range(num):
        if random.choice([True,False]):
            x = random.choice(list(fakeDict.keys()))
            ret.append([x, fakeDict[x]/fakeDict["total_cnt"]*100])
        else:
            x = random.choice(list(trueDict.keys()))
            ret.append([x, trueDict[x]/trueDict["total_cnt"]*100])
    return(ret)

print(randomWords(3))