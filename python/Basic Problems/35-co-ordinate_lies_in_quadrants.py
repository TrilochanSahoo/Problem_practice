x = int(input("Enter X co-ordinate : "))
y = int(input("Enter Y co-ordinate : "))

if (x>=0 and y>=0):
    print(x,y,"in first quadrant.")
elif (x>=0 and y<0):
    print(x,y,"in second quadrant.")
elif (x<0 and y<0):
    print(x,y,"in third quadrant.")
else:
    print(x,y,"in fourth quadrant.")

