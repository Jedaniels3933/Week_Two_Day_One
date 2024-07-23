#(f) w/ parameters establish a req variable/value for our (f) function

def personal_greeting(name):
    print(f"Hello {name}, welcome to user defined functions!")

personal_greeting("James") # Call the function with argument "James"
personal_greeting("Jane") # Call the function with argument "Jane"

person = 'Jeremy'
personal_greeting(person)   # Call the function with argument "Jeremy" Makes life easier when we need to print personalized greetings

# The same function can be used with different arguments, making it versatile and reusable.
def get_username():
    user_input= input("Whats your name?")
    return user_input   
user_name = get_username()

print(f"Hello welcome to out text based game, {user_name}!! Get ready for adventure!!")



