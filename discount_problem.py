n=int(input("Enter the number of quantity:"))
cost=n*100
if(cost>1000):
    discount=(10*cost)/100
    total_cost=cost-discount
print(total_cost)
