n=int(input("Enter the number:"))
sum_even=0
sum_odd=0
while(n>0):
    d=n%10
    if(d%2==0):
        sum_even=sum_even+d
    else:
        sum_odd=sum_odd+d
    n=n//10
print(sum_even,sum_odd)
