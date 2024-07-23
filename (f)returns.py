# The goal of functions is to produce something , take something in as an argument, and then do something with that argument.then return the output.

name = "Jeremiah"
data = type(name)
print(data)

print(type(name))   # prints String cause thats what it is- allows us to see /view return data from the (f)
#simple (f) with a return statement
def addition(a , b):
    return a + b
total = addition(5 , 5)  #must print to see the result 

print(total) #prints 10
print(addition(10 , 25 ))

#def addition1(a,b):
    #ans = a + b
    #return ans

addition(25,25) #return
#Must print to see it 
print(addition(25 , 25))

#Return a list of doubled nums
#doubler (f) takes a list of numbers as an argument and returns a list of those numbers doubled
def doubler(nums):
    doubled_nums = []
    for i in nums:
        doubled_num = i * 2
        doubled_nums.append(doubled_num)
    return doubled_nums

my_nums = [1,2,3,4,5,6,7,8,9]
dnums = doubler(my_nums)
print(dnums) #prints

# a function with no return

def greet_card(name):                  #a (f) w/o a return statement = none value
    print(f"Have a nice day, {name}!")

card_message = greet_card("Jeremiah")
print(card_message) #prints none
#Return statement ends the function execution and returns the value -  Will ignore anything after the return statement















