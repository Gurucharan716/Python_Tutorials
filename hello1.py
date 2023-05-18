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
# print(name)






