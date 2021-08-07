# EX : 60 & 72
# 60 = 2*2*3*5
# 72 = 2*2*2*3*3
# lcm = 2*2*2*3*3*5 = 360
def LCM(num1,num2):
    lcm=0
    if(num1>num2):
        lar=num1
    else:
        lar=num2
    while(True):
        if(lar%num1==0 and lar%num2 ==0):
            lcm = lar
            break
        else:
            lar=lar+1
    return lcm


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

res = LCM(num1,num2)
print("LCM of",num1,"&",num2,"is",res)