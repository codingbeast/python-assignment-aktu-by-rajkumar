#by rajkumar
mystack=[]
stacksize=3
def displaystack():
    print("Stack currently contains:")
    for item in mystack:
        print(item)
def push(raj):
    if len(mystack)<stacksize:
        mystack.append(raj)
    else:
        print("stack in overflow")
def pop():
    if len(mystack)>0:
        mystack.pop()
    else:
        print("stack in empty")
push(1)
push(2)
push(3)
displaystack()
input("press any key when ready")
push(4)
displaystack()
pop()
displaystack()
input("press any key when ready")
pop()
pop()
pop() 
displaystack()
