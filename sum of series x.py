n=int(input("Enter the value of n:"))
x=int(input("Enter the value of x:"))
i=1
sum=0
while i<=n:
    a=x**i
    a=a/i
    sum=sum+a
    i+=1
print("The sum of series is:",sum)
            
