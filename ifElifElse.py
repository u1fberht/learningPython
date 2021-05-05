favorite_color = input("Enter your favorite color: ")
cody_favorite_color = "Purple"
if favorite_color.isdigit() :
    print("Numbers are not colors, silly!")
elif favorite_color.lower() == cody_favorite_color.lower() :
    print("Hey! " + favorite_color + " is my favorite color too!\nAwesome stuff!")
else :
    print("I think " + favorite_color + " is a cool color. I, however, prefer " + cody_favorite_color.lower())

# Messing with more string functions

print("When I was younger, my favorite color was " + cody_favorite_color.replace("Purple", "Orange"))
print("This was because Commander Cody from Attack of the Clones had " + cody_favorite_color.replace("Purple", "Orange") + " accents")

# Seeing if user inputted number is even using a for loop

user_num = input("Enter a number: ")
for x in range(0, 4) :
    if user_num.isdigit() == 0 :
        user_num = input("Please enter a valid number: ")
    elif user_num.isdigit() == 1 :
        user_num = int(user_num)
        if user_num % 2 == 0 :
            print("Congratulations! You have entered an even number!")
            break
        else :
            print("Congratulations! You have entered either an odd number or a number with a decimal!")
            break

user_num = str(user_num)
if user_num.isdigit() == 0 :
        print("You have failed to enter a valid number: congratulations. Your parents have failed.")
