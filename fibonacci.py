n=int(input("Enter the range:"))
i=0
f=0
s=1
while(i<n):
    if(i<=1):
        next=i
    else:
        next=f+s
        f=s
        s=next
    print(next)
    i=i+1
