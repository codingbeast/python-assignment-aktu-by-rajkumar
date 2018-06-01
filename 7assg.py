#by rajkumar
word=input("enter the strings \n")
word=word.lower()
word_list=word.split()
raj_s=sorted(word_list)
raj_s=' '.join(raj_s)
seen=set()
pk=','.join(seen.add(i) or i for i in raj_s.split() if i not in seen)
print(pk)

