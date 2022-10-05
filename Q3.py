from re import X


def evengenrator(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1
n=int(input("enter the nunber"))
for e in evengenrator(n):
    print(e,end=" ")