# take two input as name and count letter and give length of the name and count of the letter whether it is in upper case or lower case 

# name, count_letter = input("Enter you name and count letter by , sperated: ").split(",")

# print(f"your lenght of the name is {len(name.strip())} and count of the letter {count_letter.strip()} is {name.strip().lower().count(count_letter.strip().lower())}")


# # Strip method 
# name = "    gurucharan   "
# striped_text = name.strip()+".............."
# striped_left_text = name.lstrip()+".............."
# striped_right_text = name.rstrip()+".............."

# print(striped_text)
# print(striped_left_text)
# print(striped_right_text)

# this is gurucharan --------- just commented 


# string replace 

# name = "Gurucharan is a good boy and he is good at devops"
# print(name.replace("is","was"))
# print(name.replace("is","was",1))


# finding method
# name = "Gurucharan is a good boy and he is good at devops"
# print(name.find("is"))
# print(name.find("is",12))

# is_first_postion = name.find("is")
# is_second_postion = name.find("is",is_first_postion+1)
# print(is_second_postion)


# CENTER METHOD
# name = "gurucharan"
# print(name.center(14,"*"))

# name = input("enter you name: ")
# print(name.center(len(name)+4,"*"))


# STRING IMMUTABLE
# name = "gurucharan"
# name[4] = "C"   ---> worng
# print(name)

# name = name.replace("c","C") -----> right
# print(name)


# BASIC OPERATOR

# name= "guru"
# name = name + "charan"
# print(name)                                                 -----> Day 18/05/2023 progress 

# IF ELES STATEMETS

# age = 17

# if age >=18:
#     print("Your are eligible")
# else:
#     print("you are not eligible")

# pass statement

# x = 18 

# if x ==18:
#     pass

# nested if else statement

# win_num = 60
# guess_number = int(input("enter a number for guess: "))

# if guess_number==win_num:
#     print("you win the game!...")
# else:
#     if guess_number>win_num:
#         print("number is too high...")
#     else:
#         print("number is loo low.....")

# ---------------------------------------------------------------
# import random
# win_num = random.randint(0,10)
# guess_number = int(input("enter a number for guess: "))

# if guess_number==win_num:
#     print("you win the game!...")
# else:
#     if guess_number>win_num:
#         print("number is too high...")
#     else:
#         print("number is loo low.....")

# print(f"answer is {win_num}")
# ---------------------------------------------------------------

# name = "gurucharan"
# age = 21

# if name[0]=="g" and age==21:
#     print("name and age is correct....")
# else:
#     print("name and age is not correct...")

# if name[0]=="g" or age==21:
#     print("name and age is correct....")
# else:
#     print("name and age is not correct...")                       --------> Day 19/05/2023 progress


# REVISION

# name = input("enter your name: ")
# age = int(input("enter your age: "))

# if (name[0]=="G" or name[0]=="g") and age>=18:
#     print(f"{name} is eligible because he is {age}")
# else:
#     print(f"{name} is not eligible because either his name not start with \"G\" or \"g\" nor his is age is not above 18") 


# age = int(input("enter child age: "))

# if age<=0:
#     print("invalid age input please input correct again....")
# elif 0<age<=3:
#     print("ticket is free")
# elif 3<age<=10:
#     print("ticket price is 150 rs")
# elif 10<age<=60:
#     print("ticket price is 250")
# else:
#     print("ticket price is 200")                                     -----> Day 24/05/2023 progress


# IN in if statement
# name = "gurucharan"

# if "u" in name:
#     print("present")
# else:
#     print("not present")


# CHECK EMPTY
# name = "gurucharan"

# if name:
#     print("not empty")
# else:
#     print("empty")

# name = input("Enter your name: ")

# if name:
#     print(f"Hello {name} .....")
# else:
#     print("please fill the input.....")

# While loop 
# i=1

# while i<=10:
#     print(f"hello world {i}")
#     i = i +1

# i = 1 
# total = 0

# while i<=10:
#     total = total + i
#     i = i + 1

# print(total)

# REVISION

# num = int(input("Enter a number to sum: "))

# total = 0
# i = 1

# while i<=num:
#     total = total + i
#     i = i + 1
# print(total)                                                        -----> Day 26/05/2023 progress