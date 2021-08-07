# perfect number :- number = sum of proper divisor(divisor except itself)
# EX - 28 = 1+2+4+7+14

num = int(input("Enter a number : "))
divisor = []
result=0

for i in range(1,num):
    if(num%i==0):
        print(i)
        divisor.append(i)
    
for i in range(0,len(divisor)):
    result = result + divisor[i]

if(result==num):
    print(num,"is a perfect number.")
else:
    print(num,"is not a perfect number.")