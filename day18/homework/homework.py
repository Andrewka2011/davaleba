#1) შექმენით სია სადაც გექნებათ მოცემული 5 სახელი, index ების გამოყენებით დაბეჭდეთ ცალცალკე, dont use for cycle

five_random_names=["nika" , "tea" , "luka" , "saba" , "lizi"]

print("five_random_names"[0])
print("five_random_names"[1])
print("five_random_names"[2])
print("five_random_names"[3])
print("five_random_names"[4])

#2) შექმენით სია სადაც გექნებათ მოცემული 5 სახელი, for ციკლის გამოყენებით კი დაბეჭდეთ თითოეული

five_names=["andria","sandro","dato","ana","mariami"]

for i in five_names:
    print(i)




#3)შექმენით სია სადაც გექნებათ 1-10 ჩათვლი რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ არ რიცხვების ჯამი ცალკე და ნამრავლი ცალკე

numbers=[1,2,3,4,5,6,7,8,9,10]

for numbers in numbers:
    result=result + numbers

for numbers in numbers:
    result=result * numbers

#4) 

#5)

#6)

name=("the best academy is GOA")
name=name.split(" ")
new_list = []
for word in name:
    new_word=""
    for i in word:
        if i != word[0]:
            new_word+=i
    new_list.append(new_word)
print(new_list)







