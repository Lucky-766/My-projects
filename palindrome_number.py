n=int(input("Enter the number:"))
temp=n
rev=0
while(n>0):
    ans=n%10
    rev=rev*10+ans
    n=n//10
if(temp==rev):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
