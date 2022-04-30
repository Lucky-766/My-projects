n=int(input("Enter the number:"))
rev=0
while(n>0):
    d=n%10
    rev=rev*10+ans
    n=n//10
print("Reversed number is:",rev)
