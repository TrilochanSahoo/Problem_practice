month = int(input("Enter month code : "))
year = int(input("Enter year : "))

def checkLeapYear(year):
    if ((year%4==0 or year%100!=0) and (year%400==0 or year%100!=0)):
        return True
    else:
        return False

if(month==2):
    if(checkLeapYear(year)):
        print(month,"/",year," is having 29 days.")
    else:
        print(month,"/",year," is having 28 days.")
elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print(month,"/",year," is having 31 days.")
else:
    print(month,"/",year," is having 30 days.")

