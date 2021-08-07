def prime(num):
    list = []
    for i in range(2,num):
        temp = 0
        for j in range(2,i):
            if(i%j==0):
                temp+=1
                break
        if(temp==0):
            list.append(i)
    return list


def checkSum(num):
    primeList = prime(num)
    print(len(primeList))
    for i in range(0,len(primeList)):
        for j in range(i+1,len(primeList)):
            if((primeList[i]+primeList[j])==num):
                print("Sum of",primeList[i],"&",primeList[j],"is",num)


num = int(input("Enter a number to check : "))
checkSum(num)