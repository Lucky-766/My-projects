n=int(input())
r=int(input())
nfact=1
for i in range(1,n+1):
    nfact=nfact*i
rfact=1
for i in range(1,r+1):
    rfact=rfact*i
n_rfact=1
for i in range(1,n_rfact+1):
    n_rfact=n_rfact*i
ans=nfact//(n_rfact-rfact)*rfact
print(ans)
