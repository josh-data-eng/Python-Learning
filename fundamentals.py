# DATA TYPES
from datetime import date


name = "Josh"
age = 23
student = True
height = 25.4

# PRINT FUNCTION
#print(type(name))
#print(type(age))
#print(type(student))
#print(type(height))

#ESCAPE SEQUENCE
#print('''Your Learning
      #-Python Basics
      #-Data Engineering
      #-AI''')

# INPUT FUNCTION
#first_name = input("Enter Firstname:")
#last_name = input("Enter Lastname:")
#age = input("Enter Age:")
#full_name = first_name +" " + last_name
#print(full_name)

#SLICING AND INDEXING
#full_name = "Joshua Ihimire"
#print(full_name[7])
#print(full_name[0:6])
#print(full_name[-7:])
#print(full_name[::2])

#print("-" *20)

#date = "1-5-2026"
#print(date.split("-"))
#print(date.replace("0","5"))
#print(f"my name is {full_name} iam {age} iam {height}cm tall my birthday is {date}")


#STRINGS CHALLENGES FROM CLAUDE AI

#challenge 1
user_name = input("Enter name:")
print(user_name.upper())

#challenge 2
user_hobby = "i love Learning Python"
print(user_hobby.count("o"))

#challenge 3
user_feels = " python is fun "
print(user_feels.strip())

#challenge 4
user_email = input("Enter email: ")
print(user_email.endswith("@gmail.com"))

#challenge 5
user_says = "Python is fun to learn"
print(user_says.replace(" ", "-"))

#challenge 6
word = input("Enter a Word:")
print(word[::-1])

#challenge 7
name = "big josh"
print(name.title())

#challenge 8
word = input("Enter Word:")
print(word==word[::-1])

#challenge 9
sentence = input("Enter a sentence :")
print(len(sentence.split()))

#challenge 10
