# Problem Statement – Write a program to calculate the fuel consumption of your truck.The program should ask the user to enter the quantity of diesel to fill up the tank and the distance covered till the tank goes dry.Calculate the fuel consumption and display it in the format (liters per 100 kilometers).

# Convert the same result to the U.S. style of miles per gallon and display the result. If the quantity or distance is zero or negative display ” is an Invalid Input”.

# [Note: The US approach of fuel consumption calculation (distance / fuel) is the inverse of the European approach (fuel / distance ). Also note that 1 kilometer is 0.6214 miles, and 1 liter is 0.2642 gallons.]

# The result should be with two decimal place.To get two decimal place refer the below-mentioned print statement :

# float cost=670.23;

# System.out.printf(“You need a sum of Rs.%.2f to cover the trip”,cost);

# Sample Input 1:

# Enter the no of liters to fill the tank
#            20

# Enter the distance covered
#            150

# Sample Output 1:

# Liters/100KM
#           13.33

# Miles/gallons
#           17.64

fuel = int(input("Enter the no of fill the tank : "))
if fuel<=0:
    print(fuel +"is an invalid input")
else:
    dis = int(input("Enter the distance covered : "))
    if(dis<=0):
        print(dis +"is an invalid input")
    else:
        eu_approach = round((fuel/dis)*100,2)
        print("Liters/100KM",eu_approach)
        us_approach = round((dis*0.6214)/(fuel*0.2642),2)
        print("miles/gallons",us_approach)