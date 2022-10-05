from math import gcd


def decor_coprime(hcf):
    def validation(n1,n2):
        
            a=gcd(n1,n2)
            if a==1:
               print("number are co-prime")
            else:
               print("numbers are not co prime")
        
            hcf(n1,n2)
    return validation

@decor_coprime
def hcf(n1,n2):
    print("hcf of two number is ",gcd(n1,n2))

n1=int(input())
n2=int(input())
hcf(n1,n2)
    

    
