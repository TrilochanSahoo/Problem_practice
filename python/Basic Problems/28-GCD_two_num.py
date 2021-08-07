# EX : 60 & 72
# 60 = 2*2*3*5
# 72 = 2*2*2*3*3
# gcd = 2*2*3=12

def fun_GCD(num1,num2):
    if(num1<num2):
        low = num1
    else:
        low = num2
    for i in range(1,low+1):
        if(num1 % i == 0 and num2 % i == 0):
            gcd = i
    print("GCD of",num1,"&",num2,"is",gcd)

            
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
fun_GCD(num1,num2)