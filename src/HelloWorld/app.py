# program runs from top to bottom
# NOTE: python is aCASE SENSITIVE LANGUAGE

# age = 20
# price = 19.95
# first_name = 'Bobbry'
# is_online = True
# print(age)

# patient_name = 'John Smith'
# patient_age = 20
# patient_is_new = True

# receiving input from the user

# the below line allows you to store user input in a variable

# name = input("What is your name?")

# print("Hello " + name)


#  type conversion

# birth_year = input("Enter you birth year: ")

# # NOTE: type error, trying to subtract int from string
# # to solve this problem, convert string to int

# # age = 2020 - birth_year
# age = 2020 - int(birth_year)

# print(age)

# 10 is an int
# 10.1 is a float

# built in functions that convert

# int()
# float()
# bool()
# str()

# my solution

# first = 10.1
# second = 20

# sum = first - second

# print("Here is our sum: " + str(sum))

# his solution

# first = float(input("First: "))

# second = float(input("Second: "))
# sum = first + second
# print(sum)



# course = 'Python for Beginners'
# # NOTE: this does not alter the original string, but creates a new string
# # print(course.upper())
# # below syntax returns index of found character
# # print(course.find('y'))

# # the following syntax checks if 'Python" is in the string course
# # notice the 'in' keyword
# # below returns bool value
# print('Python' in course)

# 2 different division operators

# single slash gives floating point number
# print(10 / 3)

# # double slashes will give us an integer
# print(10//3)

# exponent operator, the following expresses 10 to the 3rd power
# print(10 ** 3)


# temperature = 25


# # this is an if statement block in python, notice how it is different than JS, parenthesis
# # in python you use indentation to present a block of code
# if temperature > 30:
#     print("It's a HOT day!")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")


# KG converter program:

# weight = float(input("Enter the weight you want converted: "))

# typeConversion = input("(K)g or (L)bs: ")

# if typeConversion == ('l' or 'L'):
#     print("Weight in Kg: " + str(weight * 0.453))
# elif typeConversion == ('k' or 'K'):
#     print("Weight in Lbs: " + str(weight * 2.2))


#While loops

# i = 1
# # while i <= 1_000: #notice syntax with underscore for 1000, 1_000 is the same as 1000, just more readable
# #     print(i)
# #     i = i + 1

# while i <= 10:
#     print(i * '*') #can multiple number and string, and will repeat string based on value of number
#     i = i + 1




#Lists (same thing as an array):

# names = ["John", "Bob", "Mosh", "Sam", "Mary"]

# names[0] = 'Jon'

# # print(names[-1]) #not seen in other languages? Can do a negative index list item. -1 will give us "Mary" on the list
# #                     # represents blank item from the end of the list

# # print(names)

# print(names[0:3]) #returns all items from start index (0) UP TO the end index (3), but excluding end index



#List methods:

# numbers = [1, 2, 3, 4, 5]

# numbers.append(6)     -> adds 6 to the end of the list
#NOTE: on mac, he is able to go to view -> parameter info    with cursor inside method, displays what parameter is expected for method
#index, object of any type to be added to list
# numbers.insert(0, -1)

# numbers.remove(3)    #removes the number 3 from the list

# numbers.clear()   #clears are items from the list

# print(numbers)

# print(1 in numbers)   #print boolean for if the specific value 

# print(len(numbers))  #returns number of elements in list



#For loops:

# numbers = [1, 2, 3, 4, 5]

# for item in numbers:
#     print(item)


#The Range() function
    
# numbers = range(5)   #range(5) generates a range of numbers UP UNTIL the number that is in the parameter, last number specified always
                        #excluded

# numbers = range(5, 10)  #start and end range

# numbers = range(5, 10, 2)   # the 3rd parameter is the "step", specifies we want to go up by a specific interval

# # print(numbers)

# for number in numbers:
#     print(number)

#NOTE: can iterate over a range object using a for loop

#can just include



#Tuples
#kind of like lists, used to store a sequence of objects, but tuples are immutable (cannot be changed once created)

numbers = (1, 2, 3, 3)   #tuples signified with parenthesis instead of square brackets

numbers.count(3)