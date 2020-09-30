#! python3

# Have the user input a number. 
# Determine if the number is larger than 100 
# If it is, the output should read "The number is larger than 100" 
# (2 points)
# Inputs:
# number

# Outputs:
# "The number is larger than 100"
# "The number is smaller than 100"
# "The number is 100"

a=input("enter in your number").strip()
b=100
a=float(a)
b=float(b)

if a>b:
    print("The number is larger than 100")
elif a==b:
    print("The number is 100")
elif a<b:
    print("The number is smaller than 100")
