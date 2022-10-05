def squaregenrator(n):
    x=1
    while n:
         
      yield x
      x+=1
      n-=1
n=int(input("enter the nunber"))
for e in squaregenrator(n):
    print(e**2,end=" ")
