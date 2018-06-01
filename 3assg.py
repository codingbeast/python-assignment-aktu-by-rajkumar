#by rajkumar
a, b = 0, 1
n=20
for i in range(0, n):
    a, b = b, a + b
    print(a)
