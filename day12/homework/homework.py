# first exersize

for i in range(1,51):
    if i % 5==0:
        print(i)

#2

for i in range(2,21):
    if i % 2 == 0:
        print(i)

#3

l=1
for i in range(5,11):
    l= l * i
    print("ამ ეტაპზე ნამრავლი უდრის" , l , "ხოლო l გავამრავლეთ" , i , "-ზე" )

#4

n1=3
n1=7

u=int(input("enter a number:  "))
finaly=1
for i in  range(1 , n1 +1):
    finaly *= i

#5

u=int(input("enter a number:  "))
if u % 2 == 0:
    u /= 2
    print(u)
else:

    u = u*3 + 1
    print(u)

#6

i = 10
while i > 0:
    print(i)
    i -= 1

#7

user=input("5enter your name /or/ quit  ")
while user != "quit":
    user=input("enter your name /or/ quit  ")
#8

l = 10
x = 21
while l < x:
    if l % 2 == 0:
        print(l)
    l += 1

#9
    
u = int(input("please entar a number :  "))
while u < 0:
    print("please enter a number once again")
    print("please enter a positive number")

#10

i=1
while i<=10:
    print(i*i*i)
          