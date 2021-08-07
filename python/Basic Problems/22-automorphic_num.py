# automorphic :- number whose squre is end in the same digits as the number
# EX - 25 = 25^2 = 625 

num = int(input("Enter a number : "))
sq_num = num**2
temp = num
digit = 0
while(temp != 0):
    temp = temp // 10
    digit = digit + 1
temp = sq_num%(10**digit)
if(num==temp):
    print(num,"is an automorphic number.")
else:
    print(num,"is not an automorphic number.")