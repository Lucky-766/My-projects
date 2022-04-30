n=int(input("Enter the number:"))
fact=1
if(n<0):
    print("Factorial does not exist")
elif(n==0):
    print("Factorial of is 1")
else:
    while(n>0):
        fact=fact*n
        n=n-1
print("Factorial is:",fact)
    
