import json
textData = []
splitTextData = str()
filename = "no_punctuationText"
with open("tweets.json",encoding="UTF-8") as f:
    data = json.load(f)

for i in range(len(data)):
    textData.append(data[i]["text"])
# print(textData)
for i in textData:
    a = i.split()
    for j in a:
        splitTextData += j + " "
# print(splitTextData)

punc = '''!()-[]{};:"'\,<>./?@#$%^&*_~'''
no_punct = ""
for char in splitTextData:
    if char not in punc:
        no_punct += char
f = open(filename, "r+", encoding="UTF-8")

f.write(no_punct)


def readFile(f):
    fileObj = open(f, "r", encoding="UTF-8")
    w = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return w

newarray = readFile(filename)
splitarr = []
words = {}

for i in newarray:
    a = i.split()
    for j in a:
        if j != "RT":
            splitarr.append(j)

uniquewords = set(splitarr)
for i in uniquewords:
    words[i] = splitarr.count(i)

sort_order = sorted(words.items(), key=lambda x:x[1], reverse=True)
# print(sort_order)
result = []
for i in sort_order:
    a = str(i[0]) + " = " + str(i[1])
    result.append(a)
#print(result)

for i in range(10):
    print(result[i])

# f.truncate(0) #remore everything
f.close()