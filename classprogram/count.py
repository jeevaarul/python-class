def count(n):
    count=0
    while(n>0):
        
        n=n//10
        count+=1
    return count 
n=input("enter the value")
print(count(n))