import csv
text = open('wordlist.csv').read()
text=text.lower()
words = text.split(',')
print(words)

word_count = {}
for word in words:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1
    '''
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count '''
count = 0
for key, value in word_count.items():
    print(key)
    print(value)
    count += 1
print(count)


'''
topHundred={}
word_count_list = sorted(word_count, key=word_count.get, reverse=True)
updatedword={}
updatedword_count={}
for word in word_count_list[:100]:
    updatedword.update({word:word_count[word]})
print (updatedword)

print("dict",word_count_list[:100])
with open("topcount.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerow(['word','count'])
    writer.writerow(updatedword)
'''