#Task 1
start = int(input("Enter Start Value: "))
end = int(input("Enter End Value: "))
def describe_range(start, end, step=1):    
    for i in range(start,end):
        if i % 2==0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
if start >= end:
    print("Try again")
else:
    describe_range(start,end)

#Task 2
mylist = (6,5,20,8,10)
def summarize_numbers(myList):
    totalNum = 0
    for s in myList:
        totalNum = totalNum + s
    print(f"Count:{myList} Total: {totalNum} Avarage: {totalNum/len(mylist)} Min: {min(myList)} Max: {max(myList)}")
summarize_numbers(mylist)

#Task 3
score = int(input("Enter Score Value: "))
if 100>score>0:
    def letter_grade(score):
        if 100>=score>90:
            print(f"{score} Note is A")
        elif 90>=score>80:
            print(f"{score} Note is B")
        elif 80>=score>70:
            print(f"{score} Note is C")
        elif 70>=score>60:
            print(f"{score} Note is D")
        elif 60>=score>50:
            print(f"{score} Note is E")
        else:
            print("Note is F")
else:
    print("Invalid Grade")
letter_grade(score)




