

#

def whats_ur_name():
    thing = input("what is your name?")
    print(f"Lets welcome {thing} to our game!")
    return thing    #Critical step to make it work correctly

#whats_ur_name()
#print(whats_ur_name()) #this will print the output of the second function call'
whats_ur_name = whats_ur_name() #This will store the output of the function in a variable

print(whats_ur_name) #this will print the stored output of the function call

def whats_ur_name_2(thing):
    print(f"Welcome back {thing}!")
name = input("What is your name again?")

whats_ur_name_2(name)

