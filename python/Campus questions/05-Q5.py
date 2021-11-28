# Problem Statement  – In a theater, there is a discount scheme announced where one gets a 10% discount on the total cost of tickets when there is a bulk booking of more than 20 tickets, and a discount of 2% on the total cost of tickets if a special coupon card is submitted. Develop a program to find the total cost as per the scheme. The cost of the k class ticket is Rs.75 and q class is Rs.150. Refreshments can also be opted by paying an additional of Rs. 50 per member.

# Hint: k and q and You have to book minimum of 5 tickets and maximum of 40 at a time. If fails display “Minimum of 5 and Maximum of 40 Tickets”.  If circle is given a value other than ‘k’ or ‘q’ the output should be “Invalid Input”.

# The ticket cost should be printed exactly to two decimal places.

# Sample Input 1:

# Enter the no of ticket:35
# Do you want refreshment:y
# Do you have coupon code:y
# Enter the circle:k
# Sample Output 1:

# Ticket cost:4065.25
# Sample Input 2:

# Enter the no of ticket:1
# Sample Output 2:

# Minimum of 5 and Maximum of 40 Tickets

tickets = int(input("Enter the no of ticket:"))
if (tickets<5 or tickets>40):
    print("Minimum of 5 and Maximum of 40 Tickets")
else:
    refreshment = input("Do you want refreshment:")
    coupon = input("Do you have coupon code:")
    circle = input("Enter the circle:")
    if ((refreshment=='y' or refreshment=='n') and (coupon=='y' or coupon=='n') and (circle=='k' or circle=='q')):
        if circle=="k":
            total = tickets*75
        else:
            total = tickets*150
        # print(total)
        if(tickets>20):
            total = total*0.9
        
        if coupon=="y":
            total = total*0.98
        if refreshment =="y":
            total= total+(tickets*50)
        
        print("Ticket cost :",total)
    else:
        print("Invalid Input")