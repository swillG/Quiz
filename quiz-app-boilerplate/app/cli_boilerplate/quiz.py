from questions import QUESTIONS


def ask_question(q):
    """
    Ask a single question and return True if correct, False otherwise.
    TODO:
    - Print question + options
    - Get user input
    - Check if correct
    """
    print(q["question"])
    for options in q["options"]:
        print(f"{options}")
    # print(q["options"])
    question = input("enter your answer: ")
    if question.upper() == q["answer"]:
        print(f"you are correct. The answer is {q["answer"]}")
    else:
        print(f"you are wrong. The answer is {q["answer"]}")

    # pass


# ask_question()

def run_quiz():
    """
    Run through all questions.
    TODO:
    - Keep score
    - Loop through QUESTIONS
    - Call ask_question for each
    - Print final score
    """
    for question in QUESTIONS:
        ask_question(question)


run_quiz()
# pass
