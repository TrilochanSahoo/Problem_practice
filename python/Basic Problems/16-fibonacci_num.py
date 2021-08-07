# fibonacci number :- sum of prvious two number is next number
# EX = 0,1,1,2,3,5,8...

num = int(input("Enter number of fibonacci number: "))
first = 0
second = 1
print(num,"fibonacci numbers are :")
print(first,second,end=" ")
for i in range(2,num):
    next = first + second
    print(next,end=" ")
    first=second
    second=next