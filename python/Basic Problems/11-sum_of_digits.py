num = int(input("Enter a number : "))
temp = num
flag=0

while(num!=0):
    flag = flag + (num%10)
    num=num//10
print("sum of digits of",temp,"is",flag)

