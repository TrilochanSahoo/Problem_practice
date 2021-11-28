# XYZ Technologies is in the process of increment the salary of the employees.  This increment is done based on their salary and their performance appraisal rating.

# If the appraisal rating is between 1 and 3, the increment is 10% of the salary.
# If the appraisal rating is between 3.1 and 4, the increment is  25% of the salary.
# If the appraisal rating is between 4.1 and 5, the increment is  30% of the salary.
# Help them to do this,  by writing a program that displays the incremented salary. Write a class “IncrementCalculation.java” and write the main method in it.

# Note   :   If either the salary is 0 or negative  (or) if the appraisal rating is not in the range 1 to 5 (inclusive), then the output should be “Invalid Input”.

# Sample Input 1 :

# Enter the salary
# 8000

# Enter the Performance appraisal rating
# 3

# Sample Output  1 :

# 8800

# Sample Input  2 :

# Enter the salary
# 7500

# Enter the Performance appraisal rating
# 4.3

# Sample Output  2 :

# 9750

# Sample Input  3 :

# Enter the salary
# -5000

# Enter the Performance appraisal rating
# 6

# Sample Output  3 :

# Invalid Input

class IncrementedSalary:
    def __init__(self,salary,rating) -> None:
        self.salary = salary
        self.rating = rating
    
    def calculate(self):
        incr = 0
        if (self.rating>1 and self.rating<=3):
            incr = self.salary*0.1
        elif(self.rating>3 and self.rating<=4):
            incr = self.salary*0.25
        elif(self.rating>4 and self.rating<=5):
            incr = self.salary*0.3
        print(self.salary+incr)

salary = int(input("Enter the salary"))
rating = float(input("Enter the Performance appraisal rating"))

if(salary<0 or (rating<0 or rating>5)):
    print("Invalid Input")
else:
    res = IncrementedSalary(salary,rating)
    res.calculate()
