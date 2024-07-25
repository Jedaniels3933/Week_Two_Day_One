
operation = input("Choose an operation, 'add', 'sub', 'mult', 'div': ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

def add(num1, num2):
    return num1 + num2
if operation == 'add':
    print(add(num1, num2))

def sub(num1, num2):
    return num1 - num2
if operation == 'sub':
    print(sub(num1, num2))

def mult(num1, num2):
    return num1 * num2
if operation == 'mult':
    print(mult(num1, num2))

def div(num1, num2):
    if num2 == 0:
        print("Error: Division by zero!")
    elif num2 != 0:
        return num1 / num2
print(div(num1, num2))


print("=" * 100)
    
library = []

def add_to_library(grocery):  
    grocery = input("What is the name of item?")
    library.append(grocery)
    return library

def main():
    grocery_list = []
    flag = True
    while flag:
        ans = input('''
What would you like to do?)
1. Add a new item to list
2. View list   
3. Quit
''')
        if ans == '1':
            updated_library = add_to_library(library)
        elif ans == '2':
            library()
        elif ans == '3':
            flag = False
            print("Thank you for using this app!")  
main()