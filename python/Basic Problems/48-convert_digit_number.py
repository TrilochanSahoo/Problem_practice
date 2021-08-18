num = input("Enter a number : ")
temp1 = num

unit = ["","one","two","three","four","five","six","seven","eight","nine"]
mul_ten = ["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty"]
tenth = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

word = ''
temp = 0
length = len(num)
num = int(num)
temp=num

if(length>=4):
    word = unit[int(temp1[-4])] +" thousand "
if(length>=3):
    word =word + unit[int(temp1[-3])] +" Hundred "
if ((num%100<20) and (num%100>9)):
    word =word + tenth[(num%10)]
else:
    if (num%100>=20):
        temp=temp//10
        word =word+ mul_ten[temp%10] +" "+ unit[num%10]
    else:
        word =word + unit[num%10]
    
print(word)


