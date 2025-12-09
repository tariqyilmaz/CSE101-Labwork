#Task 1
number = int(input("Enter number: "))
def fib(n):
    if n < 0:
        raise ValueError("You entered wrong value")
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(number))

#Task2
baseYour = int(input("Enter number: "))
expYour = int(input("Enter number: "))
def power(base,exp):
    if exp < 0:
        raise ValueError("You entered wrong value")
    if exp == 0:
        return 1
    return base * power(base,exp -1)
print(power(baseYour, expYour))

#Task3
numbers = [1,2,3]
def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])
print(recursive_sum(numbers))

#Task4
def binary_search(sorted_list, target, low, high): #Devam edicek
    return 0
    
    


