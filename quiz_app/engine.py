from quiz_app.question import Question
import random

def get_valid_input(prompt, Options):
    while True:
        answer = input(prompt).lower()
        if answer in Options:
            return answer
        print(f"Invalid Input, Please enter one of: {',' .join(Options)}")

def save_score(name,score):
    score_file = open("Score.txt","a")
    score_file.write("\n\nName: " + name + "\nScore: " + str(score))

    score_file.close()

def run_quiz(questions):
    user_name = input("Enter Your Name: ")

    random.shuffle(questions)
    score = 0
    for quest in questions:
        answer = get_valid_input(quest.prompt, ["a","b","c"])
        if answer == quest.answer:
            score += 1
        else :
            print("Wrong! Correct Answer is '" + quest.answer + "'\n")
    percent = (score / len(questions)) * 100
    print(f"You got {score}/{len(questions)} correct. ({percent:.2f}%)")
    if percent >= 80:
        print("Great job!")
    elif percent >= 50:
        print("Not bad. Keep practicing!")
    else:
        print("You need more practice.")

    save_score(user_name, score) 
    