

def add_to_library(books):
author = input("Enter the author's name: ")
title = input("Enter the book's title: ")
book = [author, title]
books.append(book)

def main():   # Do this on HW then def the other (f)
    
    library = []
    flag = True
    while flag:
        ans = input('''
What would you like to do?
1. Add a new book
2. View all books
3. Quit
''')
        
        if ans == '1':
            pass
        elif ans == '2':
            display_books()
        elif ans == '3':
            flag = False
            print("thanks for using our book management system!")

                            