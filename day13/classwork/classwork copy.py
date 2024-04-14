#1
#number

num1=int(input("please enter a number:  "))
if num1 > 0:
    print("num1 is positive")
if num1 < 0:
    print("num1 is negative")
else:
    if num1 == 0:
        print("num1 is 0")

#2
#age

age=int(input("please enter your age"))

if age >=0 and age < 18:
    print("you are a child")
else:
    print("you are an adult")