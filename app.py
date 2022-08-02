# Console Log 
print("Hello world")

# Variable
first_name = "Asif"
age = 33
print('My name is ' + first_name)
print(age)

## Input (written in the terminal)
# input_name = input("Name a country ? ")
# print('Selected country : ' + input_name)

# # Type of variable 
# birthday = input("Enter your birthday ")
# # parseInt
# formatToInt = int(birthday)
# age = 2022 - formatToInt
# print("Your age is " + str(age))

# float() = convert number like 10.5
# bool() to convert to a boolean 

# String in Python 
course = "Python for Beginners"
upperCaseString = course.upper()
print(upperCaseString)
# finds first index
index = course.find("o")
print(index)
# replace 
replace = course.replace("for", "4")
print(replace)
# include 
include = "Python" in course
print(include)

# comparaison operator
number = 3 == "3"
print(number)
# === does not exist ! here number is false in JS, it would have been true 

#logical operation
# && : and
# || : or 
# ! : not 
price = 19
print(price > 10 and price < 50)

# if statement
# need to indent the code and add : 
temperature = 8
if temperature > 30: 
    print("hot day")
elif temperature >= 10 and temperature <= 29:
    print("warm day")
else: 
    print("cold day")

# while loop
i = 1
while i <= 5: 
    print(i * "*")
    i = i + 1

# array
names = ["Asif", "Luffy", "Zorro", "Traw", "Marco", "Ace"]
names[3] = "Trawfalgar"
names.append("Sanji") # push
names.insert(1, "Kaido") # splice
names.remove("Zorro") 
# names.clear() = vide l'array names = []
# in = includes "Asif" in names
# len(names) = names.length
print(names[0], 
    names[-1], 
    names[0: 3], 
    names, "Asif" in names, 
    len(names)
)

# for loop
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# range function
# from 15 to 25 with 5 added each time
listNumber = range(15, 25, 5)
for list in listNumber:
    print(list)

# tuples 
# can't change tuples
listTwo = (1, 2, 3)