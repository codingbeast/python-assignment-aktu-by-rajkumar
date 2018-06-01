#by rajkumar
word=input("enter the strings \n")
word=word.lower()
word_list=word.split()
print(word_list)
word_set=set(word_list)
freq={}
for word in word_set:
    freq[word]=word_list.count(word) /float(len(word_list))
    print(freq)
