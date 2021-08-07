def create_map(bin_oct_map):
    bin_oct_map["000"] = "0"
    bin_oct_map["001"] = "1"
    bin_oct_map["010"] = "2"
    bin_oct_map["011"] = "3"
    bin_oct_map["100"] = "4"
    bin_oct_map["101"] = "5"
    bin_oct_map["110"] = "6"
    bin_oct_map["111"] = "7"


def bin_to_oct(num):
    length = len(num)

    if(length % 3==1):
        num = "00"+num
    elif(length % 3 == 2):
        num = "0"+num
    else:
        num=num
    bin_oct_map={}
    create_map(bin_oct_map)
    i = 0
    octal = ""

    while(True):
        octal = octal + bin_oct_map[num[i:i+3]]
        i = i + 3
        if(i == len(num)):
            break
        
    return octal


num = input("Enter a binary number : ")
print("octal number of",num,"is",bin_to_oct(num))