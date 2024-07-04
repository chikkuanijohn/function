def add(a,b):
    return a+b
def sub(a,b):
    return a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b
def numbers():
    a=int(input("enter first num"))
    b=int(input("enter second num"))
    return a,b
while True:
    print("1.add \n2.sub \n3.mul \n4.div \n5.exit ")
    ch=int(input("enter your choice"))
    if ch==1:
        a,b=numbers()
        print(add(a,b))
    if ch==2:
        a,b=numbers()
        print(sub(a,b))
    if ch==3:
        a,b=numbers()
        print(mul(a,b))
    if ch==4:
        a,b=numbers()
        print(div(a,b))
    if ch==5:
        break                     


    
