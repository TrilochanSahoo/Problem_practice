def dec_to_bin(num):
    bin = ""
    while(num!=0):
        bin = str(num % 2)+bin
        num = num//2
    return bin
    

num = int(input("Enter a decimal number : "))
print("Binary of",num,"is",dec_to_bin(num))