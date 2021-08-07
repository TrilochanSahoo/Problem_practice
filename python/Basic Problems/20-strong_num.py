# strong :- number = sum of factoral of digits
# 145 = 1! + 4! + 5! 
def fact(num):
    if(num==1):
        return 1
    else:
        return num * (fact(num-1))


def isStrong(num):
    result = 0
    while(num!=0):
        result = result + fact(num%10)
        num=num//10
    return result

num = int(input("Enter a number :"))
res = isStrong(num)
# print(res)
if(res == num):
    print(num,"is a strong number.")
else:
    print(num,"is not a strong number.")
