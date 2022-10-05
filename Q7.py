from re import A
from turtle import Turtle


def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b


it=fib()

for e  in range(int(input())):
    print(next(it))