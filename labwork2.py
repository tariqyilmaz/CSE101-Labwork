#task 1
drink = "Latte"
size = "Grande"
price = 85.5

print(f"You order: {size} {drink} - {price}")

#task 2
number_of_steps = int(input("Number of steps:"))
def calculate_remaining_steps(number_of_steps):
    return 10000 - number_of_steps
print(f"Remaining steps to reach your goal: {calculate_remaining_steps(number_of_steps)}")

#task 3
title = "Inception"
duration = 148
rating = 8.8

print(f"Movie: {title}, Duration: {duration} minutes, Rating: {rating}/10. I think it's a great movie!")

#task 4
notebook = 25
pen = 15
eraser = 10
print(f"Total cost: {notebook + pen + eraser}TL")

#task 5
coffee = 60
transportation = 45
food = 77

print(f"Total daily expenses: {coffee + transportation + food}TL")

#task 6
petName = "Buddy"
petAge = 5
petType = "Dog"
print(f"My pet's name is {petName}, it is a {petType} and it is {petAge} years old.")

#task 7
meal = "Burger"
restaurant = "BurgerBurger"
delivery_time = 25
print(f"I ordered a {meal} from {restaurant}. It will arrive in {delivery_time} minutes.")

#task 8
readingPages = 30
setGoal = 100
def pages_left(readingPages):
    return setGoal - readingPages
print(f"Pages left to read to reach your goal: {pages_left(readingPages)}")

#task 9
city = "Bursa"
temperature = 22
condition = "sunny"
print(f"The weather in {city} is currently {condition} with a temperature of {temperature}°C.")

#task 10
name = "Ankara"
population = 5600000
area = 25706
print(f"{name} has a population of {population} and covers an area of {area} square kilometers.")

#task 11
battery_percentage = 35
if battery_percentage < 20:
    print("Battery low, please charge your device.")
else:
    print("Battery level is enough.")

#task 12
temperature = 28
if temperature > 25:
    print("It's a hot day!")
else:
    print("The weather is normal.")

#task 13
grade = 85
if grade > 60:
    print("You passed the exam!")
else:
    print("You failed the exam.")

#task 14
isMember = True
orderAmount = 120
if isMember:
    if orderAmount > 100:
        print("You get a 10% discount!")
else:
    print("No Member.")

#task 15
isRaining = True
temperature = 18
if isRaining and temperature < 20:
    print("Wear a jacket and take an umbrella!")
elif isRaining and temperature >= 20:
    print("Just take an umbrella!")
else:
    print("No need for a jacket or umbrella.")
    



