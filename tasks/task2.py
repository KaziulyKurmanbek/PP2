import math
num = int(input())  
numbers = list(map(int, input().split()))  
max1=float('-inf')
max2=float('-inf')
for a in numbers:
    if a  > max1:
        max2 = max1
        max1 = a
    elif a>max2 and a<max1:
        max2 = a
print(max2)

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given  scores. 
# Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.