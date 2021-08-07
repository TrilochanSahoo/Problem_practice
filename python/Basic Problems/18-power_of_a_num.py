base = int(input("Enter base :"))
expo = int(input("Enter exponent : "))

result = 1
for i in range(1,expo+1):
    result = result * base

print(base,"to the power",expo,"is",result) 