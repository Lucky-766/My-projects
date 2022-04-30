n=int(input("Enter the number:"))
i=1
while i<=n:
    j=1
    while j<=i:
        if i==1:
            print(1,end=" ")
        elif i==j or j==1:
            print(i-1,end=" ")
        else:
            print(0,end=" ")
        j=j+1
    print()
    i=i+1
