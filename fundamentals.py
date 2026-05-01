# DATA TYPES
name = "Josh"
age = 23
student = True
height = 25.4

# PRINT FUNCTION
print(type(name))
print(type(age))
print(type(student))
print(type(height))

#ESCAPE SEQUENCE
print('''Your Learning
      -Python Basics
      -Data Engineering
      -AI''')

# INPUT FUNCTION
#first_name = input("Enter Firstname:")
#last_name = input("Enter Lastname:")
#age = input("Enter Age:")
#full_name = first_name +" " + last_name
#print(full_name)

#SLICING AND INDEXING
full_name = "Joshua Ihimire"
print(full_name[7])
print(full_name[0:6])
print(full_name[-7:])
print(full_name[::2])

print("-" *20)

date = "1-5-2026"
print(date.split("-"))
print(date.replace("0","5"))
print(f"my name is {full_name} iam {age} iam {height}cm tall my birthday is {date}")