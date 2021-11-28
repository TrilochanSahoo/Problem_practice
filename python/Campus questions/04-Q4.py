# Problem Statement – FOE college wants to recognize the department which has succeeded in getting the maximum number of placements for this academic year. The departments that have participated in the recruitment drive are CSE,ECE, MECH. Help the college find the department getting maximum placements. Check for all the possible output given in the sample snapshot

# Note : If any input is negative, the output should be “Input is Invalid”.  If all department has equal number of placements, the output should be “None of the department has got the highest placement”.

# Sample Input 1:

# Enter the no of students placed in CSE:90
# Enter the no of students placed in ECE:45
# Enter the no of students placed in MECH:70
# Sample Output 1:

# Highest placement
# CSE

# Sample Input 2:

# Enter the no of students placed in CSE:55
# Enter the no of students placed in ECE:85
# Enter the no of students placed in MECH:85
# Sample Output 2:

# Highest placement
# ECE

# MECH

# Sample Input 3:

# Enter the no of students placed in CSE:0
# Enter the no of students placed in ECE:0
# Enter the no of students placed in MECH:0
# Sample Output 3:

# None of the department has got the highest placement
# Sample Input 4:

# Enter the no of students placed in CSE:10
# Enter the no of students placed in ECE:-50
# Enter the no of students placed in MECH:40
# Sample Output 4:

# Input is Invalid

cse = int(input("Enter the no of students placed in CSE:"))
ece = int(input("Enter the no of students placed in ece:"))
mech = int(input("Enter the no of students placed in mech:"))

if (cse<0 or ece<0 or mech<0):
    print("Input is Invalid")
elif (cse==ece==mech):
    print("None of the department has got the highest placement")
else:
    print("Highest placement:")
    if(cse>=ece and cse>=mech):
        print("CSE")
        if(cse==ece):
            print("ECE")
        if(cse==mech):
            print("MECH")
    elif(ece>=cse and ece>=mech):
        print("ECE")
        if(ece==cse):
            print("CSE")
        if(ece==mech):
            print("MECH")
    elif(mech>=ece and mech>=cse):
        print("MECH")
        if(mech==ece):
            print("ECE")
        if(cse==mech):
            print("CSE")
    
    
