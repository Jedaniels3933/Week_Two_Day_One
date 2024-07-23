#scope of variables = variables defined inside a function are only accessible within that function.

#Global = anywhere outside of a (f) or a loop
#  and Local scope - which vars are accessable 

    # Global scope: variables defined outside a function are accessible within the entire program.
    # Local scope: variables defined inside a function are only accessible within that function.
#Global var = 
x = 7 # Can access anywhere in the code
a = "Words"
alist = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']

if x:
    print(x)

    #Local created inside of a (f) or LOOP

def local_func():
    y = 10 #Local var -  Try to use y somewhere else wont work

    print(x)

local_func()
print(y) # Will throw an error


