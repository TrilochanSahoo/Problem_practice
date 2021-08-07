def oct_to_dec(num):
    length = len(num)
    num = int(num)
    dec=0
    for i in range(0,length):
        dec = dec+(num%10)*(8**i)
        num = num //10
    return dec


num = input("Enter a number : ")
print("Decimal of",num,"is",oct_to_dec(num))