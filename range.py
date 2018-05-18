names = []
for i in range(10):
  names.append(input("Enter student number {}:".format(i)))
welcome_str = "Welcome {} to akirachix"
for i in range(10):
  print(welcome_str.format(names[i]))