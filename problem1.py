#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"
import math
a=input("enter in a number ").strip()
a=int(a)
b= a%2
if b==1:
    print("the number is odd")
if b==0:
    print("your number is even")
