import urllib.request

#A Apple Pie - book
url = 'https://www.gutenberg.org/cache/epub/15809/pg15809.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
# print(text) # for testing
# print(type(text)) #string

"""
#for individual counts

print(x)
count = 0 
for word in x: 
    if word == "it":
        count += 1
print(count)
"""

#frequency
x = text.split()
dict = {}
for word in x:
    if word not in dict:
        dict[word] = 1
    else: 
        dict[word] += 1

# print(dict)

#top 10 word count
sortedDict = sorted(dict.items(), key = lambda y: y[1], reverse = True) #lambda function that takes one parameter y
for i in range(10):
    print(sortedDict[i])


