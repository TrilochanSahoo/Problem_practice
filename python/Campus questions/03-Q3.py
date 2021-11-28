# Problem Statement – Ritik wants a magic board, which displays a character for a corresponding number for his science project. Help him to develop such an application.
# For example when the digits 65,66,67,68 are entered, the alphabet ABCD are to be displayed.
# [Assume the number of inputs should be always 4 ]

# Sample Input 1:

# Enter the digits:
# 65
# 66
# 67
# 68
# Sample Output 1:

# 65-A
# 66-B
# 67-C
# 68-D

# Sample Input 2:

# Enter the digits:
# 115
# 116
# 101
# 112
# Sample Output 2:

# 115-s
# 116-t
# 101-e
# 112-p

letter=[]
print("Enter the digits:")
for i in range(4):
    char = int(input())
    letter.append(char)

print()
for i in range(4):
    print(letter[i],"-",chr(letter[i]))