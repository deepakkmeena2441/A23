from re import A


def fibgenrator(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
for e in fibgenrator(int(input("enter the nunber"))):
    print(e,end=" ")
    