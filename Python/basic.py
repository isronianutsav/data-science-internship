# PYTHON BASICS 
# ===============================

import copy   # for shallow & deep copy

# *************** Variables & Strings
__ = "ram"
print(__)

text = "sample example"
print("hello i am doing,", text)


# *************** Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)

# *************** Type Checking
x = 10
y = 10.5
z = "Python"

print(type(x))
print(type(y))
print(type(z))

# *************** Numbers & Arithmetic
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)

# *************** If – Elif – Else
num = 15

if num > 20:
    print("Number is greater than 20")
elif num == 15:
    print("Number is exactly 15")
else:
    print("Number is less than 15")

# *************** For Loop
for i in range(1, 6):
    print("for loop value:", i)

# *************** While Loop
count = 1
while count <= 3:
    print("while loop value:", count)
    count += 1

# *************** List
marks = [90, 85, 78]
print("Marks list:", marks)

marks.append(88)
print("After append:", marks)

for m in marks:
    print("Mark:", m)

# *************** Tuple
subjects = ("Math", "Physics", "Chemistry")
print("Subjects:", subjects)

for sub in subjects:
    print("Subject:", sub)

# *************** Set (Basics)
numbers = {1, 2, 3, 3, 4}
print("Set values (unique):", numbers)

numbers.add(5)
print("After add:", numbers)

numbers.remove(2)
print("After remove:", numbers)

# *************** Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# *************** Set Copy (Shallow Copy Concept)
setA = {10, 20, 30}
setB = setA.copy()

setB.add(40)

print("Original set:", setA)
print("Copied set:", setB)

# NOTE: Sets store immutable elements → deep copy not required

# *************** Dictionary
student = {
    "name": "Ram",
    "roll": 101,
    "branch": "CSE"
}

print("Student info:", student)
print("Name:", student["name"])

for key, value in student.items():
    print(key, ":", value)

# *************** Shallow Copy (List)
list1 = [[1, 2], [3, 4]]
list2 = list1.copy()

list2[0][0] = 99

print("Original list (shallow):", list1)
print("Copied list (shallow):", list2)

# *************** Deep Copy (List)
list3 = copy.deepcopy(list1)

list3[0][0] = 100

print("Original list (deep):", list1)
print("Copied list (deep):", list3)

# *************** Shallow Copy (Dictionary)
dict1 = {
    "name": "Ram",
    "marks": [80, 90]
}

dict2 = dict1.copy()
dict2["marks"][0] = 99

print("Original dict (shallow):", dict1)
print("Copied dict (shallow):", dict2)

# *************** Deep Copy (Dictionary)
dict3 = copy.deepcopy(dict1)
dict3["marks"][0] = 100

print("Original dict (deep):", dict1)
print("Copied dict (deep):", dict3)

# *************** Function
def greet(name):
    print("Hello", name)

greet("Ram")
greet("Isronian")
