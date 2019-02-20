
name_list = ["John", "Vikil", "Steven"]

print("Enter your name")
user_input = input()

if user_input in name_list:
    print("Hey {}! Welcome to the club!".format(user_input))
else:
    print("Who goes there!?")    
