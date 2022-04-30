n=int(input("Enter the number:"))
i=1
while i<=n:
    j=n
    while j>=i:
        print((n+1)-j,end=" ")
        j=j-1
    print()
    i=i+1
