def amstrong(n):
    temp=0
    sum=0
    num=n
    while(n>0):
        temp=n%10
        n=n//10
        sum+=temp**3
    if(sum==num):
        print("the number is amstrong")
    else:
        print("the number is not an amstrong")
n=input("enther the number:")
print(amstrong(n))