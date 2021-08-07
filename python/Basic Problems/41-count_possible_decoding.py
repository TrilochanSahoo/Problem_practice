num = input("Enter a number : ")
length = len(num)
num = int(num)
count = 0
string = ""
for i in range(1,length+1):
    count = num%10
    string = chr(count+64)+string
    num = num//10
print(string)