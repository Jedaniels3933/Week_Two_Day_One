# Built in (f) functions
#Bookmarked in fav (f) functions

#==-=-=-=-=-=-=-=-=-=
#print:::: (): prints data to the screen so is visible to the user
# sep , end, file and flush
# sep: separator, end: end of line, file: file to write to, flush: flush the buffer
# Given as key word arguments 
print('string','string2')  # prints two strings separated by a space
print('string1','string2',sep = '!!!!!!!!!') #adding !!! changes from default of single space or comma

# \n: newline character         \ = forward slash     / = backward slash

print('string1\n')   #will press enter after printing string1
print('After 1 line of space')

print('string1\n\n')   #will press enter twice after printing string1
print('After 2 lines of space')                                                 
print('string1\n\n\n')   #will press enter 3 times to print
print('After 3 lines of space')

print('=' * 100)
#\t: tab space adds a tab
print('this is\t\t\t\t\t','seperated') # Every t = 4 spaces or Tab

# \\ = backslash character- to use a literal \\ Works eith way
print("This string should now have a back slash\\")
print("This string should now have a back slash//")


words = " add"
print("We can" + words + " strings together")

# Formatted Strings= 

#name = "Alice"
#age = 30
# = using .format() create string using these variables
#print("Name: {}, Age: {}" .format(name, age))
#print("Name: {}, \nAge: {}".format(name ,  age))

# f-string = more pythonic and efficient way of formatting strings

# use the f keyword followed by curly braces {}
#print(f"Name: {name}, \nAge: {age}")   #Modern Version

#Input(): Used to take user input from the user
#name = input("What is your name? ") #Returns a value after its called
#print(f"Hello, {name}!")
# type() function can be used to return the type of data stored in a variable

#isinstance(var, type):
num = 10 
print(isinstance(num, int)) # True

# len() : returns the length of an iterable object
message = "Hello"
print(len(message)) # Returns 5 - the number of characters in the string "H E L L O" 5

#abs(): returns the absolute value of a number
number = -5 
print(abs(number))   #Returns 5 the absolute value of -5

#round(): rounds a number to a specified number of decimal places
#must be a decimal above .5, for ex 4.51 in order to round up 
number = 4.51
print(round(4.51))

#sum(): returns the sum of all elements in an iterable
numbers = [1,2,3,4,]
print(sum(number))
#min(): returns the smallest item in an iterable
print(min(numbers))

#pow(<num>), <to the power of>) : returns the power of a number
print(pow(2,3)) #output 8 

#divmod(): return a tuple containing the quotient and the remainder of the division
print(divmod(10,3)) # output (3, 1)

# Max -  re do this one 











     
