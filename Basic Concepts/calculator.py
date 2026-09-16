while True :            #Loop Will Continue after each iteration
    a =int(input())
    c = input()
    if c =='=':
        break;
    elif c !="=":
        b = int(input())
    
      
#DELETING THE VALUE OF INPUT
    if input() =='xx':
             del a
             del b
#PRINTING THE OUTPUT
    if c=="+":
        print(a+b)
    elif c=='-':
        print(a-b)
    elif c=='*':
        print(a*b)
    elif c=='/':
        print(a/b)


   