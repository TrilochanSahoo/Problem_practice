frac1 = input("Enter first fraction (a/b) : ")
frac2 = input("Enter second fraction (a/b) : ")
flag = frac1.split("/")
n1 = int(flag[0])
d1 = int(flag[1])
flag = frac2.split("/")
n2 = int(flag[0])
d2 = int(flag[1])

if(d1==d2):
    n3 = n1+n2
    d3 = d1
else:
    n3 = (n1*d2)+(n2*d1)
    d3 = d1*d2

print("addition of",frac1,frac2,"is",n3,"/",d3)