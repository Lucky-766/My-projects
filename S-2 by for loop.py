n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print((n+1)-j,end=" ")
        j+=1
    print()
    i+=1
