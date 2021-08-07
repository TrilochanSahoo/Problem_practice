num = int(input("Enter a number : "))
temp = 0
for i in range(2,num):
    if (num % i == 0):
        temp += 1
        break
        
if (num==1):
        print(num," is not a prime.")
elif(temp == 0):
    print(num," is a prime.")
else:
    print(num," is not a prime.")