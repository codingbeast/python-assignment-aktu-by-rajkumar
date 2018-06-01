#by rajkumar
inraj=input("enter the string \n")
list1=inraj.split()
print("the list is :", list1)
print("length of list is:",len(list1))
list1.append('rajkumar')
print("length of list is:",len(list1))
del list1[0]
print(list1)
