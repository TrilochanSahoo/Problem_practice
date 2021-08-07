# factor = a number divided by numbers
# EX :- 12 = 1,2,3,4,6,12

num = int(input("Enter a number : "))
print("Factors of",num,"is : ")
for i in range(1,num+1):
    if(num % i == 0):
        print(i,end=" ")
    