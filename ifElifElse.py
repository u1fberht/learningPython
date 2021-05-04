favorite_color = input("Enter your favorite color: ")
cody_favorite_color = "Purple"
if favorite_color.isdigit() :
    print("Numbers are not colors, silly!")
elif favorite_color.lower() == cody_favorite_color.lower() :
    print("Hey! " + favorite_color + " is my favorite color too!\nAwesome stuff!")
else :
    print("I think " + favorite_color + " is a cool color. I, however, prefer " + cody_favorite_color.lower())
    
