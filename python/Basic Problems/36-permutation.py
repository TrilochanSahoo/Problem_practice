def fact(num):
    if(num==1):
        return 1
    else:
        return num*(fact(num-1))
    

person = int(input("Enter no of person : "))
seat = int(input("Enter no of seats available : "))

way = fact(person)/fact(person-seat)

print(way,"no of ways",person,"can sit in",seat,"seats.")