# abundant number :- sum of proper divisor > number
# EX : 12 = 1+2+3+4+6=16>12

num = int(input("Enter a number : "))
# divisor = []
sum = 0
for i in range(1,num):
    if(num%i==0):
        # divisor.append(i)
        sum = sum + i

# for i in range(0,len(divisor)):
#     sum = sum + divisor[i]
if(sum>num):
    print(num,"is an abundant number.")
else:
    print(num,"is not an abundant number.")