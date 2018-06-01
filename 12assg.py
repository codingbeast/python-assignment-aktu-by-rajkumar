#by rajkumar
myqueue=[]
queuesize=3
def displayqueue():
    print("queue currently contains:")
    for item in myqueue:
        print(item)
def push(raj):
    if len(myqueue)<queuesize:
        myqueue.insert(0,raj)
    else:
        print("queue in overflow")
def pop():
    if len(myqueue)>0:
        myqueue.pop()
    else:
        print("queue in empty")
push(1)
push(2)
push(3)
displayqueue()
input("press any key when ready")
push(4)
displayqueue()
pop()
displayqueue()
input("press any key when ready")
pop()
pop()
pop() 
displayqueue()
