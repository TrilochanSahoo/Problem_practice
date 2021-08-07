def fact(num):
    if(num==1):
        return 1
    else:
        return (num*(fact(num-1)))


num = int(input("Enter a number : "))
result = fact(num)
print("Factorial of",num,"is",result)