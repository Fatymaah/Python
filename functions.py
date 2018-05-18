def welcome_student(name):
    welcome_str="Hi {} welcome to Akirachix"
    return welcome_str.format(name)
    
name=input("Enter a name:")
print(welcome_student(name))
print(welcome_student("Rehema"))
print(welcome_student("Lauren"))
print(welcome_student("Ivy"))