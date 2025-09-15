from quiz import load_questions, run_quiz
from storage import save_score, show_past_scores

def main():
    print("=== Welcome to the Quiz App ===")
    name = input("Enter your name: ").strip()

    # Show past scores
    show_past_scores()

    # Load questions
    questions = load_questions()

    # Run quiz
    score, total = run_quiz(questions)

    # Save score
    save_score(name, score, total)

if __name__ == "__main__":
    main()
