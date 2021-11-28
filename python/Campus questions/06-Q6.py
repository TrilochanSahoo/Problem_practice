# Problem Statement – Rhea Pandey’s teacher has asked her to prepare well for the lesson on seasons. When her teacher tells a month, she needs to say the season corresponding to that month. Write a program to solve the above task.

# Spring – March to May,
# Summer – June to August,
# Autumn – September to November and,
# Winter – December to February.
# Month should be in the range 1 to 12.  If not the output should be “Invalid month”.

# Sample Input 1:

# Enter the month:11
# Sample Output 1:

# Season:Autumn
# Sample Input 2:

# Enter the month:13
# Sample Output 2:

# Invalid month
month = int(input("Enter the month:"))
switcher = {
    1:"Winter",
    2:"Winter",
    3:"Spring",
    4:"Spring",
    5:"Spring",
    6:"Summer",
    7:"Summer",
    8:"Summer",
    9:"Autumn",
    10:"Autumn",
    11:"Autumn",
    12:"Winter"
}
season = switcher.get(month,"Invalid month")
if season == "Invalid month":
    print("Invalid month")
else:
    print("Season:",season)