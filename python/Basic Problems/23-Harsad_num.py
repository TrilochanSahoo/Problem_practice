# harsad number :- number divisible by sum of digit of a number
# EX = 408 = number/sum of digits = 408%12=0

num = int(input("Enter a number : "))
temp = num
sum = 0
while(temp != 0):
    sum = sum + (temp % 10)
    temp = temp // 10
if(num % sum == 0):
    print(num,"is a harsad number.")
else:
    print(num,"is not a harsad number.")