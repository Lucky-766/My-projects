n=int(input("Enter the number:"))
i=1
while i<=n:
    s=1
    while s<=n-1:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1
