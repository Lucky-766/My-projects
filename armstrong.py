n=int(input("Enter the number:"))
sum=0
temp=n
while(n>0):
    d=n%10
    sum=sum+d**3
    n=n//10
if(temp==sum):
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")
    
