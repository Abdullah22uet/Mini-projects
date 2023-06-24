import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

further = "yes"
while 1:
    length_password = int(input("Enter the length of password : "))
    count_password = int(input("How many passwords you want to generate : "))

    for i in range(0 , count_password):
        password = ""
        for j in range(0 , length_password):
            ran_word = random.choice(characters)
            password = password + ran_word
        print(f"Password {i+1} = {password}")
    further = input("Whether you want to generate more passwords? (yes or any key) or (no) : ")
    if further == "no" or further == "No":
        break

print("")
print("Thanks regards Random Password Generator")