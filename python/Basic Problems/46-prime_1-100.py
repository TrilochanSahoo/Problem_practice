print("Prime number from 1-100 are : ")
for i in range(2,101):
    num = i
    count = 0
    for j in range(2,num):
        if(num%j==0):
            count += 1
            break
    if(count==0):
        print(i,end=" ")
        

