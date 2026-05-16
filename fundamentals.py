for number in range(0, 11, 2):
    print(number)

fruits = ["banana", "lemon", "cherry", "mango", "orange"]
for fruit in fruits:
    print(fruit)

scores = [20, 33, 78, 18]
total = 0
for score in scores:
    total += score
    print(total)
print("Final total:", total)

files = [' report.csv', 'DATA.csv',' josh.jpg ']
for file in files:
    file = file.strip().lower().replace('.jpg', '.csv')
    print(f"processed {file}")