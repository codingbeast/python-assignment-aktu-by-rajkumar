#by rajkumar
raj=input(" ")
raj1=raj.split()
r2=len(raj1)
ra=raj1[0]
print(ra,end=" ")
for i in range (1,r2):
    pk=raj1[i].split()
    j=" ".join(pk)
    rk=j.replace(j[0],'$')
    print(rk,end=" ")
print(" ")
