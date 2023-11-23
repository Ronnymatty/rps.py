import math
import sys

num1 = input("enter any number :")
num = int(num1)
if num == 0 :
    sys.exit("you can not enter 0 try again")

numsqr = math.sqrt(num)

print(f"the square root of {num} is {numsqr}")
