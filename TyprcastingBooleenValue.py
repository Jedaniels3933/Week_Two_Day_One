#bool(): converts a value to a boolean value

print(bool(0)) #output false
print(bool(1)) #output true

print(bool('')) #output false  #EMPTY STRING

print(bool([])) #output false  #EMPTY LIST

print(bool(0))

names = []
names1 = ["D", "E"]
print(bool(names)) #output False
print(bool(len(names)))

if names1:
    print("The list is not empty")
else:
    print("The list is empty")