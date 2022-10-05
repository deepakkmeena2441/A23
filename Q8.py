


def prime(n):
    
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    else:
        return True

def genrator():
    n=2
    while True :
        if prime(n):
            yield n
        n+=1

it=genrator()

for i in range(int(input())):
    print(next(it))




