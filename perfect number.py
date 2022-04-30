def perfect(n):
    if n<1:
        return false
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n
first=int(input())
last=int(input())
print("prfect numbers in given range are:")
for i in range(first,last+1):
    if perfect(i):
        print(i,end=" ")
