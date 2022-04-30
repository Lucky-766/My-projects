n=int(input("Enter the number:"))
count=0
for i in range(2,(n//2+1)):
    if(n%i==0):
        count+=1
        break
if(count==0):
    print("It is prime.")
else:
    print("It is not prime.")
    
    
            
          
      
