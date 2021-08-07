def isArmstrong(num):
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
    if(sum==temp):
        return True
    else:
        return False


lower = int(input("Enter lower range : "))
upper = int(input("Enter upper range : "))

for i in range(lower,upper):
    num = isArmstrong(i)
    if(num):
        print(i,end=" ")