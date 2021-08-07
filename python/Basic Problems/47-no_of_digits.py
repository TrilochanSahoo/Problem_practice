num = int(input("Enter an integer : "))
digit = 0
temp = num
while(temp!=0):
    num = num//10
    digit += 1
print(num,"is a",digit,"number.")