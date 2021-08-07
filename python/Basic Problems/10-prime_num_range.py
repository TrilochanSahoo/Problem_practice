lower = int(input("Enter lower range : "))
upper = int(input("Enter upper range : "))
print("The prime number from ",lower," to ",upper," is :")
for num in range(lower,upper):
    temp = 0
    for i in range(2,num):
        if(num%i==0):
            temp+=1
            break
    if (num==1):
        print(end="")
    elif (temp==0):
        print(num,end=" ")