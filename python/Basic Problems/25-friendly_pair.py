# friendly pair = numbers having same index ratio between sum of divisior by number
# EX : 6 ,28 
# 6 = (1+2+3+6)/6=2
# 28 = (1+2+4+7+14+28)/28=2 
def isFriendlyPair(num):
    sum=0
    for i in range(1,num+1):
        if(num%i==0):
            sum=sum+i
    return (sum/num)


num1 = int(input("Enter first number in pair : "))
num2 = int(input("Enter second number in pair : "))

val1 = isFriendlyPair(num1)
val2 = isFriendlyPair(num2)
if(val1==val2):
    print(num1,",",num2,"are friendly pair.")
else:
    print(num1,",",num2,"are not friendly pair.")
