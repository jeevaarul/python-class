def oddneven(n):
    oddc=0
    evenc=0
    while(n>0):
        temp=(n%10)
        if(temp%2==0):
            evenc+=1
        else:
            oddc+=1
        n=n//10
    return evenc,oddc
n=input("enter the value")
print(oddneven(n))