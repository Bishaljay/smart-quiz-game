def run_quiz():
    print("🎉 Welcome to the Smart Quiz Game! 🎉")
    print("-------------------------------------")

    questions = [
        {
            "question": "1. What is the capital of Nepal?",
            "options": ["A. Kathmandu", "B. Pokhara", "C. Lalitpur", "D. Biratnagar"],
            "answer": "A"
        },
        {
            "question": "2. Which programming language are you learning in Code in Place?",
            "options": ["A. Java", "B. C++", "C. Python", "D. JavaScript"],
            "answer": "C"
        },
        {
            "question": "3. What is 5 + 7?",
            "options": ["A. 10", "B. 12", "C. 14", "D. 15"],
            "answer": "B"
        },
        {
            "question": "4. Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Earth", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "5. How many days are there in a week?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "C"
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}.")

    print("\n-------------------------------------")
    print("🏆 Quiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 60:
        print("🎉 Congratulations! You Passed!")
    else:
        print("📚 Keep Practicing and Try Again!")

run_quiz()