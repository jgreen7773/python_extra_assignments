first_name = "Zen"
last_name = "Coder"
age = 27

print(f"My name is {first_name} {last_name} and I am {age} years old.")


# string.format()

print("My name is {} {} and I am {} years old."
      .format(first_name, last_name, age))

# OLD FORMATTING STYLE

hw = "Hello %s" % "world"
py = "I love Python %d" % 3
print(hw, py)

name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))

# Basically the s stands for string, the d stands for digit, and the % by
# itself is a space


x = "hello world"
print(x.title())

# title is a method, same as .format() ...but varies slightly in its
# functionality/use.


x.upper()
x.lower()
# x.count(substring)

# def find_all_indexes(input_str, substring):
#     # 12 = []
#     length = len(input_str)
#     while index < length:
#         i = input_str.find(substring, index)
#         if i == -1:
#             return 12
#         # 12.append(i)
#         # index = i + 1
#     return 12


# # First attempt to create valid parentheses check funtion
# def validparanth(var1, var2, var3, var4, var5, var6):

#     # attempting to store count inside of object "paranthcount"
#     paranthcount = {
#         ")": 0
#         "(": 0
#         "]": 0
#         "[": 0
#         "}": 0
#         "{": 0
#     }

#     # a loop to run through the whole length of the document
#     while index < len.__doc__:
#         index++
#         if index == ")":
#             paranthcount.")" += 1
#         if index == "(":
#             paranthcount."(" += 1
#         if index == "]":
#             paranthcount."]" += 1
#         if index == "[":
#             paranthcount."[" += 1
#         if index == "}":
#             paranthcount."}" += 1
#         if index == "{":
#             paranthcount."{" += 1

# print(paranthcount)


# method i researched/pulled from the internet (modified)


# Python3 code to Check for
# balanced parentheses in an expression
# define searchable characters "("   "{"   "["   "]"   "}"   ")"
opened_list = ["[", "{", "("]
closed_list = ["]", "}", ")"]


# Function to check parentheses
def check(myDoc):
    stack = []
    for i in myDoc:
        if i in opened_list:
            stack.append(i)
        elif i in closed_list:
            pos = closed_list.index(i)
            if ((len(stack) > 0) and
                (opened_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


# # Driver code
# string = "{[]{()}}"
# print(string, "-", check(string))

# string = "[{}{})(]"
# print(string, "-", check(string))

# Python3 code to Check for
# balanced parentheses in an expression
def check(expression):

    opened_tup = tuple('({[')
    closed_tup = tuple(')}]')
    map = dict(zip(opened_tup, closed_tup))
    queue = []

    for i in expression:
        if i in opened_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != que.pop():
                return "Unbalanced"
    return "Balanced"

# # Driver code
# string = "{[]{()}}"
# print(string, "-", check(string))


# Python3 code to Check for
# balanced parentheses in an expression
def check(my_string):
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    return not my_string

# # Driver code
# string = "{[]{()}}"
# print(string, "-", "Balanced")
#         if check(string) else "Unbalanced")


# FORMAT FOR for loops
for x in range(0, 10, 1):
    # x= iterate variable, 0= startPoint, 10= stopPoint, 1= ++


# LOOPS through LISTS
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz


# loop print through list auto
for v in my_list:
    print(v)
# output: abc, 123, xyz


# loop print through DICTIONARIES auto
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language


# loop print through dictionary VALUES auto
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python


# OTHER METHODS for printing KEY:VALUE pairs
for key in capitals.keys():
    print(key)
# to iterate through values
for val in capitals.values():
    print(val)
# to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)


# WHILE
# LOOPS
# While loops are good "while" a certain condition is true
# This for loop:
for count in range(0,5):
    print("looping - ", count)
# Is the same as this while loop:
count = 0
while count < 5:
    print("looping - ", count)
    count += 1
# The important thing about while loops:
while <expression>:
    # do something, including progress towards making the expression False. Or else we'll never get out of this loop!


# ELSE
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")
# Notice always that the variable to store something is placed at the beginning of the statement.
# If I wrote y - 1 = y, we are not storing the iteration into the variable y, but rather trying to store y inside y-1.


# Loops, breaks, returns, and continues:            CONTROL FLOW:
# Control Flow is the cornerstone of most programming languages

# the BREAK statement exits the current loop prematurely.
    # When loops are "nested", the break will exit only from the innermost loop
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r


# the CONTINUE statement immediately returns control to the beginning of the loop
    # Basically, it rejects everything in the loop below its designated location
        # Useful when you want to skip specific iterations, but still keep looping to the end
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i
y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:   # This line only executes on a clean exit from the while loop (not a break)
    print("Final else statement")
# output: 3, 2, 1


