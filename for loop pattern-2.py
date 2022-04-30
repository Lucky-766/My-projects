n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i:
            print(j,end=" ")
        elif j<i:
            print(" ",end=" ")
        else:
            print(j,end=" ")
    print()
    continue
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(n+j-i,end=" ")
    print()
        
