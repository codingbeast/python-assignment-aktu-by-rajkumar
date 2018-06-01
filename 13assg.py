#by rajkumar
f=open("/root/Desktop/raj.txt","w+")
f.write("Hello i am raj \n hello world")
f.close()
f=open("/root/Desktop/raj.txt","r+")
values=f.read()
f.close()
print(values)
