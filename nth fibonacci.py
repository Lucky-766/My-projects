n=int(input("Enter the position:"))
i=3
f=1
s=1
c=0
while i<=n:
    c=f+s
    f=s
    s=c
    i=i+1
print(n,"th fibonacci number is:",c)

