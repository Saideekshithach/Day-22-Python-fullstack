'''while True:
    def cal():
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        option=int(input(choose the option:
                                    1.add
                                    2.sub
                                    3.mul))
        if option==1:
            c=a+b
            #print("sum is",a+b)
            return c
        elif option==2:
            c=a-b
            #print("diff is",a-b)
            return c
        elif option==3:
            c=a*b
            #print("product is",a*b)
            return c
        else:
            print("Invalid option")
    print(cal())
    '''

'''def add():
    s=a+b
    print(s)
def sub():
    s=a-b
    print(s)
def mul():
    s=a*b
    print(s)
while True:
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    c=int(input(choose the option:
                                        1.add
                                        2.sub
                                     3.mul))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()
    else:
        print("invalid option")
'''
'''
def splitbill():
    n=int(input("enter no of friends:"))
    amount=int(input("enter amount:"))
    share=amount/n
    #print("amount for each person {}".format(share))
    #print(f"amount for each person {share}")
    return share
print(splitbill())'''

    
def splitbill():
    n=int(input("enter no of friends:"))
    amount=int(input("enter total amount:"))
    share=amount/n
    print("your bill is {}".format(share))
    print(f"your bill is {share}")
    print(f"your bill is {amount/n}")
    print("your bill is {}".format(amount/n))
splitbill()

'''

def add(a,b):
    s=a+b
    return s 

a=int(input())
b=int(input())
print(add())

'''
