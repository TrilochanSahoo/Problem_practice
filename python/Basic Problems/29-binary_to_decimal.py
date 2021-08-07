def bin_to_dec(var):
    temp = var
    length = len(var)
    var=int(var)
    dec = 0
    for i in range(0,length):
        dec = dec + ((var%10)*(2**i))
        var = var // 10
    print("Decimal of",temp,"is",dec)


var = input("Enter binary digit : ")
bin_to_dec(var)

