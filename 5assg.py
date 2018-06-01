#by rajkumar
raj=input("Enter the a string:\n")
l=len(raj)
if(l>=3):
    if(raj[-3]+raj[-2]+raj[-1]=='ing'):
        print(raj+'ly')
    else:
        print(raj+'ing')
else:
    print(raj)
