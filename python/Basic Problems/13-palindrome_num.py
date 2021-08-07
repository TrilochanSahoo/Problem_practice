# palindrome :- number = reverse number 
num = int(input("Enter a number : "))
rev_num = 0
temp = num
count = 0
while(num != 0):
    num = num // 10
    count = count + 1
# print(count)
num = temp
for i in range(count,0,-1):
    rev_num = rev_num + ((num%10)*(10**(i-1)))
    # print(rev_num)
    num = num // 10

if(temp == rev_num):
    print(temp,"is a palindrome number.")
else:
    print(temp,"is not a palindrome number.")