#Quiz Task1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! Next year you will be {age+1} years old")

#Quiz Task2
numbers = list(map(float, input("Enter three numbers with space: ").split()))
print("Number               Square")
print("---------------------------")
for i in range(3):
    print(f"{numbers[i]}         {numbers[i]**2:.2f}")


#Quiz Task3
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
totalNumber = a + b
newCount = 0
if totalNumber >= 50:
    print(f"Sum: {totalNumber}")
else:
    while totalNumber < 50:
        newNumber = int(input("Enter next number:"))
        totalNumber += newNumber
        newCount +=1
    print(f"Sum: {totalNumber} Count: {newCount}")

#Task1
class Book:
    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title.strip
        self.author = author.strip
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
print(Book())
print(Book("Ortadoğu", "Bernard Lewis"))

#Task2
class Book:
    totalCreated = 0
    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title.strip
        self.author = author.strip
        Book.total_created += 1
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
print(Book())
print(Book("Ortadoğu", "Bernard Lewis"))
print(f"Total books created: {Book.total_created}")
#Task3
class Book:
    totalCreated = 0
    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title.strip
        self.author = author.strip
        Book.total_created += 1
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"   
    def save_books(books, path):
        with open(path, "w", encoding="utf-8") as f:
            for b in books:
                f.write(f"{b.title} | {b.author}\n")
    def load_books(path):
        result = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if "|" not in line:
                    continue
                title, author = [part.strip() for part in line.split("|", 1)]
                result.append(Book(title, author))
        return result
    print(load_books("books.txt"))
print(Book())
print(Book("Ortadoğu", "Bernard Lewis"))
print(f"Total books created: {Book.total_created}")




