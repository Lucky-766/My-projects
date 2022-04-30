def updateSum(n):
    if n==0:
        return n
    else:
        return pow((n%10),order)+updateSum(n//10)
n=int(input())
order=len(str(n))
sum=updateSum(n)
if sum==int(n):
    print(n,"is armstrong.")
else:
    print(n,"is not armstrong.")
    
