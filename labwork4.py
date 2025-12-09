#Hocam başka projelerle boğuştuğum için hepsine bakamadım. Bir iki tane ekleme yaptım. Puan kırmazsanız sevinirim:) 4 ü kendim yaptım söylemiştim btw

#task1
i = 1
while i < 21:
    if i % 2 == 0:
        print("Even:", i)
    else:
        print("Odd:", i)
    i += 1

#task2
numberzero = 0
num = int(input("Enter a number: "))
plus = 1
while num != 0:
    numberzero = numberzero + int(num)
    num = int(input("Enter a number: "))
    plus += 1

#task3
score = input("Enter exam score: ")
score = int(score)
if 80 <= score < 100:
    print("AA")
elif 60 <= score < 80:
    print("BB")
elif 40 <= score < 60:
    print("CC")
elif 20 <= score < 40:
    print("DD")
elif 0 <= score < 20:
    print("FF")

#task4
wordList = []
wrongList = []
sentence = input("Enter a sentence: ")
wordSplit = sentence.split()
for word in wordSplit:
    if word not in wordList:
        wordList.append(word)
    else:
        wrongList.append(word)
for wrongWord in wrongList:
    if wrongWord in wordList:
        wordList.remove(wrongWord)
newSentence = " ".join(wordList)
print("New sentence:", newSentence)
    
#task5
foodList = []
isWanting = True
listing = input("Do you want make shopingList: ")
while isWanting:
    if listing == "yes":
        food = input("Enter a food item: ")
        foodList.append(food)
        listing = input("Do you want add item: ")
    else:
        isWanting = False
        print("Your shopping list:", foodList)
    

#task6
number = int(input("Enter a number: "))
for i in range(1, number+1):
    if number % i == 0:
        print(i)

