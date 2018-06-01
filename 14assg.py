#by rajkumar
import shutil
f=open("/root/Desktop/raj.txt","w+")
f.write("hello friend i am rajkumar \n nice to meet u abcd")
f.close()
shutil.copyfile("/root/Desktop/raj.txt","/root/Desktop/test.txt")
f=open("/root/Desktop/test.txt","r+")
values=f.read()
f.close()
print(values)
