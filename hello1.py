# take two input as name and count letter and give length of the name and count of the letter whether it is in upper case or lower case 

name, count_letter = input("Enter you name and count letter by , sperated: ").split(",")

print(f"your lenght of the name is {len(name.strip())} and count of the letter {count_letter.strip()} is {name.strip().lower().count(count_letter.strip().lower())}")


# Strip method 
name = "    gurucharan   "
striped_text = name.strip()+".............."
striped_left_text = name.lstrip()+".............."
striped_right_text = name.rstrip()+".............."

print(striped_text)
print(striped_left_text)
print(striped_right_text)

# this is gurucharan ---------