#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math
num1=float(input("Enter the first number "))
num2=float(input("Enter the second number "))
num3=float(input("Enter the third number "))
# hyp is meant to represent the side with longest length, not necessarily the hypotenuse (if it's not a right triangle)
if num1>=num2 and num1>=num3:
    hyp=num1
elif num2>=num1 and num2>=num3:
    hyp=num2
elif num3>=num1 and num3>=num2:
    hyp=num3
if hyp==num1:
    s1=num2
    s2=num3
elif hyp==num2:
    s1=num1
    s2=num3
elif hyp==num3:
    s1=num1
    s2=num2
hyp2=math.sqrt(s1**2 + s2**2)
deci=hyp2/hyp
frac=abs(deci)-1
final=abs(frac)*100
coHyp=round(math.degrees(math.acos((s1*s1 + s2*s2 - hyp*hyp)/(2*s1*s2))),5)
coS1=round(math.degrees(math.acos((hyp*hyp + s2*s2 - s1*s1)/(2*hyp*s2))),5)
coS2=round(math.degrees(math.acos((hyp*hyp + s1*s1 - s2*s2)/(2*hyp*s1))),5)
if (coHyp>90 or coS1>90 or coS2>90) and final>2:
    obtuse="that is an obtuse triangle"
    print(obtuse)
    quit()
elif coHyp<90 and coS1<90 and coS2<90:
    acute="that is an acute triangle"
    print(acute)
    quit()

elif final<=2 :
    print("that is a right triangle")

