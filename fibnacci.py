#python program for fibonacci series usin generator
def fibo():
    first,second= 0,1
    
    while True:
        yield first
        first,second = second,first+second


g=fibo()
n=int(input("Enter range of number"))
for i in range(n):
    print(next(g))