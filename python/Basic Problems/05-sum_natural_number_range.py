lower = int(input("Enter value for lower range : "))
upper = int(input("Enter value for upper range : "))
result = 0 
for i in range(lower, upper+1):
    result = result + i

print(f"sum of {lower} to {upper} is {result}")