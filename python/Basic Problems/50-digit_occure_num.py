num = int(input("Enter a number: "))
temp = num
unit = {}
while(temp!=0):
    digit = temp%10
    if digit in unit:
        unit[digit]+=1
    else:
        unit[digit]=1
    temp = temp//10

for key in unit:
    print(key," is present ",unit[key]," times")

