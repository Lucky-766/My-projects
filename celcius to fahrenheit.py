def converttocelcius(s,e,w):
    for i in range(s,e+1,w):
        c=int((i-32)*(5/9))
        print(i,c)
s=int(input())
e=int(input())
w=int(input())
converttocelcius(s,e,w)
