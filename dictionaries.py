# Day 13: Dictionaries in Python
# Dictionary stores data in key : value form

# Creating a dictionary
student = {
    "name": "Rawal",
    "age": 18,
    "course": "Python"
}

print("Student dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Using get() method
print("Course:", student.get("course"))

# Updating values
student["age"] = 19
print("Updated age:", student["age"])

# Adding new key-value pair
student["city"] = "Jaipur"
print("After adding city:", student)

# Removing key
student.pop("course")
print("After removing course:", student)

# Looping through dictionary
print("\nKeys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey - Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# User input dictionary
user = {}

n = int(input("How many details you want to add? "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user[key] = value

print("User dictionary:", user)
