#Task 1
colors = []
for i in range(3):
    askColor = input("What are your favorite 3 colors? ")
    colors.append(askColor)
print("Your favorite colors are:", colors)
print("List length:", len(colors))

#Task 2
pets = ["cat", "dog", "fish"]
otherPet = pets[0]
pets[0] = pets[2]
pets[2] = otherPet
print("Updated pet list:", pets)

#Task 3
items = ["milk", "bread"]
newItem = input("Enter an item: ")
items.append(newItem)
items.remove(items[0])
print("Updated items list:", items)

#Task 4
numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)
print(f"Min Value:", {min(numbers)}, "Max Value:", {max(numbers)})

#Task 5
nums = [2, 4, 6, 8, 10, 12]
firstThree = nums[:3]
lastTwo = nums[-2:]
print(f"İlk üç sayı: {firstThree}")
print(f"Son iki sayı: {lastTwo}")

#Task 6
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
dictionarty = {"name": name, "age": age, "city": city}
print("Information:", dictionarty)

#Task 7
contacts = {"Ada": "555-1234", "Ali": "555-9876"}
newContactName = input("Enter contact name: ")
print("Contact number:", contacts.get(newContactName, "Not found"))

#Task 8
wordDict = {}
sentence = input("Enter a sentence: ")
wordSplit = sentence.split()
for word in wordSplit:
    wordDict[word] = len(word)
print("Words:", wordDict)

#Task 9
import math
points = {}
currentPoint = 0
for i in range(3):
    point = int(input("Enter points: "))
    points[f"Lesson {i+1}"] = point
print("Average Point:", math.ceil(sum(points.values()) / len(points)))


