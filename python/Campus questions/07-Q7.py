# Problem Statement – To speed up his composition of generating unpredictable rhythms, Blue Bandit wants the list of prime numbers available in a range of numbers.Can you help him out?

# Write a java program to print all prime numbers in the interval [a,b] (a and b, both inclusive).

# Note

# Input 1 should be lesser than Input 2. Both the inputs should be positive. 
# Range must always be greater than zero.
# If any of the condition mentioned above fails, then display “Provide valid input”
# Use a minimum of one for loop and one while loop
# Sample Input 1:

# 2

# 15

# Sample Output 1:

# 2 3 5 7 11 13

# Sample Input 2:

# 8

# 5

# Sample Output 2:

# Provide valid input

def isPrime(num):
    if num>1:
        temp=0
        for i in range(2,num):
            if (num%2==0):
                temp+=1
                break
        if(temp==0):
            print(num,end=" ")


lr = int(input())
hr = int(input())
if ((hr>0 and lr>0) and hr>lr):
    for i in range(lr,hr):
        isPrime(i)
else:
    print("Provide valid input")