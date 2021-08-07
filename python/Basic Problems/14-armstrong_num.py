# armstrong number :- number =sum of digits raised to the power of digit
# EX :- 371 = 3^3 + 7^3 + 1^3  

num = int(input("Enter a number :"))
temp = num
sum = 0
count = 0

while(num != 0):
    num=num//10
    count = count+1
num = temp

for i in range(count,0,-1):
    sum = sum + ((num%10)**count)
    num = num//10

if(sum == temp):
    print(temp,"is an armstrong number.")
else:
    print(temp,"is not an armstrong number.")
