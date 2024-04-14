#1

budget = int(input("what is your budget :  "))

cost = int(input("please enter the price:  "))


if budget >= cost:
    print("purchase is complite")
else:
    print("payment canseled")

#2

registered_password = "2011"

password = input("Please enter your password: ")

while password != registered_password:
    password = input("Please enter your password again: ")
    if password == registered_password:
        print("You have accses on your account")
    else:
        print("You have entered wrong password, please try again")


#3


start = int(input("Please enter starting value: "))
end = int(input("Please enter ending value: "))
step = int(input("Please enter step value: "))

for i in range(start,end,step):
    print(i)


#4
    

side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The data is correct.")
else:
    print("The data is incorrect. Please try again.")
          

#5
          

s1 = int(input("Please enter first side: "))
s2 = int(input("Please enter second side: "))
s3 = int(input("Please enter third side: "))


is_valid = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

while is_valid != True:
    s1 = int(input("Please enter first side: "))
    s2 = int(input("Please enter second side: "))
    s3 = int(input("Please enter third side: "))

    is_valid = s1 + s2 > s3


#6

operation = input("Please enter operation (+,-,*,/): ")
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("operation is not valid")
    print("you are an adult")