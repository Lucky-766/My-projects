n=int(input("Enter the number:"))
p=1
r=0
while n>0:
    d=n%2
    r=r+d*p
    p=p*10
    n=n//2
print(r)
