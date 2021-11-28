# Problem Statement –

# IIHM institution is offering a variety of courses to students. Students have a facility to check whether a particular course is available in the institution. Write a program to help the institution accomplish this task. If the number is less than or equal to zero display “Invalid Range”.

# Assume maximum number of courses is 20.

# Sample Input 1:

# Enter no of course:
# 5

# Enter course names:
# Java

# Oracle

# C++

# Mysql

# Dotnet

# Enter the course to be searched:
# C++

# Sample Output 1:

# C++ course is available

# Sample Input 2: 

# Enter no of course:
# 3

# Enter course names:
# Java

# Oracle

# Dotnet

# Enter the course to be searched:
# C++

# Sample Output 2:

# C++ course is not available

# Sample Input 3:

# Enter no of course:
# 0

# Sample Output 3:

# Invalid Range
course = int(input("Enter no of course:"))
if(course == 0):
    print("Invalid Range")
else:
    course_list = []
    for i in range(course):
        name = input()
        course_list.append(name)
    check = input("Enter the course to be searched:")
    if(check in course_list):
        print(check,"course is available.")
    else:
        print(check,"course is not available")