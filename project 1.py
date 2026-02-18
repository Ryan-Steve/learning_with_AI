print("Enter your name:")
name = input()
print(f"\n Hello,{name}")
print("Answer the following questions:<3")
score = 0
questions =[
    {"question":"1. Which month has 28 days?","answer":"all"},
    {"question": "2. John's mother has three sons: January,February and ?","answer":"John"}
]

for question in questions:
    print(question["question"])
    users_answer = input()
    if users_answer.capitalize() == question["answer"].capitalize():
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is:",question["answer"])
        print( )

print(f"\n Your final score is {score}/2")

if score == 2:
    print("You are very smart")
else :
    print("Nice attempt, you almsost got it")

print("\n Thank you for playing the quiz game, by $tevieee")
