from quiz_app.question import Question
from quiz_app.engine import run_quiz

question_prompts = [
    "1. What does 'CPU' stand for?\n(a) Central Processing Unit\n(b) Computer Power Unit\n(c) Central Program Utility\n\n",

    "2. Which of these is a programming language?\n(a) HTML\n(b) Python\n(c) HTTP\n\n",

    "3. What symbol is used to start a comment in Python?\n(a) //\n(b) <!-- -->\n(c) #\n\n",

    "4. What is the result of 5 // 2 in Python?\n(a) 2.5\n(b) 2\n(c) 3\n\n",

    "5. Which data structure uses FIFO (First In, First Out)?\n(a) Stack\n(b) Queue\n(c) Tree\n\n",

    "6. Which of these is **not** a valid data type in Python?\n(a) integer\n(b) float\n(c) real\n\n",

    "7. What keyword is used to define a function in Python?\n(a) def\n(b) func\n(c) function\n\n",

    "8. What does RAM stand for?\n(a) Random Access Memory\n(b) Readable Assigned Memory\n(c) Remote Access Memory\n\n",

    "9. Which of these is used to repeat a block of code?\n(a) if\n(b) for\n(c) def\n\n",

    "10. What is a correct syntax to create a dictionary in Python?\n(a) {}\n(b) []\n(c) ()\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "a")
]

run_quiz(questions)