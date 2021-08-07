user_input = int(input("Enter a number : "))
result = 0
for i in range(1, user_input+1):
    result = result + i

print(f"sum of {user_input} natural number is {result}")
