print("Hello My Dear Friends")
print("Welcome to my world")
print("+++++++++++  K B C ++++++++++++++")

# Questions and answers
questions = [
    "What is My Name? \n A. Manish       B. Kashyap?",
    "What is your Age? \n A. 34          B. 19",
    "How are you? \n A. Fine           B. Confused",
    "I am your friend? \n A. Maybe!     B. Yes",
    "How can I tell you? \n A. I don't know B. You are the Best"
]

correct_answers = ["a", "b", "a", "a", "b"]

# Initialize user answers and money
user_answers = []
money = 0

# Loop through questions
for i in range(len(questions)):
    print(questions[i])
    while True:
        ans = input("Your Answer (A/B): ").strip().lower()
        if ans in ["a", "b"]:
            user_answers.append(ans)
            break
        else:
            print("Invalid answer! Please enter 'A' or 'B'.")
    print()

# Calculate the score
for user_answer, correct_answer in zip(user_answers, correct_answers):
    if user_answer == correct_answer:
        money += 500
        print("Correct! You earn 500.")
    else:
        money -= 100
        print("Wrong! You lose 100.")

# Final result
print("\nYour Answers: ", user_answers)
print("Total Money: ", money)
