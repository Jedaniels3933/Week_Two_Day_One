#Parameters = non basic have only learned basic so far-
#basic parameters are the ones that are passed directly to the function when it/'s called
def name_printer(first, middle, last):
    print(f"Hello, {first} {middle} {last}!")

#Positional arguments = position of argument determines which parameter becomes the value of in our (f) = function

name_printer("Jeremiah", "Alan", "Daniels") #Jeremiah is the first name, Alan is the middle name, and Daniels is the last name
#Keyword arguments = keyword arguments are like named arguments that are passed to the function when it's called
name_printer("Daniels", "Alan" , "Jeremiah") # =====  #Postional

#keyword arguments : we can explicitly state which parameter takes which value

name_printer(last = "Daniels", first = "Jeremiah", middle = "Alan") #Keyword in blue

#Default parameters = if a parameter isn't provided when the function is called, it will use the default- gives parameter a default value if nothing is passed into the (f)

def greeting(name = "World"):
    print(f"Hello, {name}!")

greeting()

# *args: allows us to pass an arbitrary number of positional arguments to a function. #Unknown number of arguments brought into the (f) as a tuple

def vet_hands(staff, *vols):
    print(f"On staff today we have {staff[0]} and {staff[1]}!!!")
    if vols:
        print("They will be assisted by the following volunteers:")
        for i in vols:
            print(i)
vet_hands(["Dr. Adam", "Dr. Jones"] , "Dylan" , "Travis", "Grace", "Josh", "Walter", "Phillip", "Dennis", "Derrick", "Moses", "Jeremiah", "Gamel", "Dylan", "Derek", "Sophia", "Samuel", "Ryan", "Luis", "Jacob", "Isaac", "Hayden", "Eric", "Beth", "Morty", "Jerry", "Rick", "Summer", "Space Beth")
         
#   **kwargs: allows us to pass an arbitrary number of keyword arguments to a function.

def routine(**daily_events):
    print(daily_events)

routine(morning = "Wake up, brush teeth, and eat" , mid_morning = "Walk dog" , afternoon = "Grading and prep for class", evening = "In class", dinner_time = "Eat again", night = "Sleep")  #Looping through the dictionary and printing each key-value pair















