import nltk  #Natural Language Toolkit
def readFile(f):
    fileObj = open(f, "r", encoding="UTF-8")
    w = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return w

newarray = readFile("no_punctuationText")
splitarr = []
noun = []
words = {}

for i in newarray:
    a = i.split()
    for j in a:
        if len(j) !=1 and len(j) !=2 and len(j) !=3:
            splitarr.append(j)

#print(splitarr)
ans = nltk.pos_tag(splitarr)  #list of tags
#print(ans)


for i in range(len(ans)): # checking if it is a noun or not
    val = ans[i][1]
    if (val == 'NNP'):
        noun.append(ans[i][0])
# print(noun)

uniquewords = set(noun)
for i in uniquewords:
    words[i] = noun.count(i)

sort_order = sorted(words.items(), key=lambda x:x[1], reverse=True)
result = []
for i in sort_order:
    a = str(i[0]) + " = " + str(i[1])
    result.append(a)
for i in range(10):
    print(result[i])