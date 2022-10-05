s={eval(e) for e in input("enter the number").split(",")}

for e in iter(s):
    try:
        print(e,end=" ")
    except StopIteration:
        break

