def dec_to_oct(num):
    oct=""
    while(num!=0):
        oct = str(num % 8) + oct
        num = num//8
    return oct


num = int(input("Enter a decimal number : "))
print("Octal of",num,"is",dec_to_oct(num))