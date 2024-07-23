#Created a (f) to tell us the teacher and listing the names of students - must define each variable before using it.

def class_info(instructor, students):
    print(f"This class is taught by {instructor}.")
    class_size = len(students)
    print(f"It has {class_size} students.")
    for i in students:
        print(i)

students_152 = ["Gamel", "Jeremiah", "Moses", "Travis", "Derrick", "Dennis", "Dylan", "Derek"]
class_info("Travis", students_152)

students_153 = ["Eric", "Hayden", "Isaac", "Jacob", "Luis", "Ryan", "Samuel", "Sophia"]

class_info("Ryan", students_153)

students_250 = ["Rick", "Jerry","Morty","Beth","Summer", "Space Beth"]
class_info("Mr Poopy Butthole" , students_250)

#Note: The above code defines the class_info function, then creates three classes with their respective students.

def book_info(title, author):
    print(f"{title} by {author} has been bookmarked.")




