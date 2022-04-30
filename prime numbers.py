n=int(input("Enter the number:"))
i=2
count=0
while(i<=n):
    if(n%i==0):
        count+=1
    i=i+1
    break
if(count==0):
    print(n,"is prime")
else:
    print(n,"is not prime")
    
