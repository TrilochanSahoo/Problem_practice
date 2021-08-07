# EX : 60 & 72
# 60 = 2*2*3*5
# 72 = 2*2*2*3*3
# hcf = 2*2*3=12

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
low = 0
factor = []
if(num1<num2):
    low = num1
else:
    low = num2

for i in range(1,low+1):
    if(num1 % i == 0 and num2 % i == 0):
        factor.append(i)

print("HCF of",num1,"&",num2,"is",factor[-1])
