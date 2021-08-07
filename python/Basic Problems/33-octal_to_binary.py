def oct_to_bin(num):
    octal_map = {
        0: "000",
        1: "001",
        2: "010",
        3: "011",
        4: "100",
        5: "101",
        6: "110",
        7: "111"
    }
    bin = ""
    while(num!=0):
        bin = octal_map[num%10] + bin
        num = num//10
    return bin


num = int(input("Enter a number : "))
print("Binary of",num,"is",oct_to_bin(num))