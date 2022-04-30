a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
sum=0
if a>b:
    temp=a
    a=b
    b=temp
while a<b:
    if a%2==0:
        sum=sum+a
    a=a+1
print("Sum of all even terms:",sum)
