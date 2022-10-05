from re import T
import re


def decor_sides(perimeter):
    def valdation(l):
        for e in l:
            if e>0:
                print("sides of traingles is valid ")
            else:
                print("sides of traingle are not valid")
                break
                
        else:
            perimeter(l)
        

    return valdation;   


          
        
        
        
        

            
        
            
@decor_sides     
def perimeter(l):
    print("perimeter if traingle is",sum(l))



print("lsit shold contain only three elements")
l=[eval(e) for e in input().split(",")]
perimeter(l)

