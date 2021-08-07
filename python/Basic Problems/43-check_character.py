char = input("Enter a character : ")
if(ord(char)>64):
    if(ord(char)<123):
        print("Enterd character is an alphabet")
    else:
        print("Enterd character is not an alphabet")
else:
    print("Enterd character is not an alphabet")