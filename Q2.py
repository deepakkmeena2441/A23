from re import X


def oddgenrator(n):
    x=1
    while n:
      yield x
      x+=2
      n-=1



n=int(input("enter the number"))
for e in oddgenrator(n):
    print(e,end=" ")