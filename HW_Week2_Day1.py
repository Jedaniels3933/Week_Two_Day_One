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
 

 