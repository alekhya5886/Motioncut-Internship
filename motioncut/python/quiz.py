import random

def ask_question(question, options, correct_option):

    print(question)

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        user_input = input("Enter the number of your answer: ")

        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= len(options):
                break

        print("Invalid input. Please enter a valid option.")

    user_answer = options[user_input - 1]
    return user_answer.lower() == correct_option.lower()

def run_quiz(questions):

    score = 0

    for question, options, correct_option in questions:
        if ask_question(question, options, correct_option):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_option}\n")

    print(f"Quiz completed. Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_questions = [
        ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
        ("Which programming language is this quiz written in?", ["Java", "Python", "C++", "JavaScript"], "Python"),
        ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        ("What is the capital of India", ["Mumbai", "Delhi", "Chennai", "Kolkata"], "Delhi"),
    ]

    random.shuffle(quiz_questions)

    run_quiz(quiz_questions)
