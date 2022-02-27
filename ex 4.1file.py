filename = "file_with_text"
#
#
# def remove_punc(string):
#     punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     for ele in string:
#         if ele in punc:
#             string = string.replace(ele, "")
#     return string
#
# with open(filename, 'r', encoding="utf-8") as f:
#     data = f.read()
# with open(filename, "w+", encoding="utf-8") as f:
#     f.write(remove_punc(data))
#

def readFile(f):
    fileObj = open(f, "r")
    w = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return w

newarray = readFile(filename)
splitarr = []
words = {}

for i in newarray:
    a = i.split()
    for j in a:
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
result.pop(0)
#print(result)

for i in range(10): #need to change to 10
    print(result[i])