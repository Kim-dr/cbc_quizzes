import random  # For selecting random questions
import time    # For timing how long the user takes per question
import sys     # Imported but not used (can be removed if unnecessary)

# ----------------- QUESTION BANK -----------------
# Dictionary holding categorized science questions for Grade 6, 7, 8
# Each question includes the question text, multiple choices, and the correct answer key (a/b/c/d)
question_bank = {
    "Grade 6": [
        {"question": "What do we use to see distant objects in space?", "options": ["Microscope", "Telescope", "Periscope", "Binoculars"], "answer": "b"},
        {"question": "Which organ pumps blood in the human body?", "options": ["Lungs", "Liver", "Heart", "Kidney"], "answer": "c"},
        # ... [Remaining Grade 6 questions]
    ],
    "Grade 7": [
        {"question": "What is the function of red blood cells?", "options": ["Fight disease", "Carry oxygen", "Digest food", "Control movement"], "answer": "b"},
        {"question": "Which nutrient helps build body tissues?", "options": ["Fats", "Carbohydrates", "Proteins", "Vitamins"], "answer": "c"},
        # ... [Remaining Grade 7 questions]
    ],
    "Grade 8": [
        {"question": "What type of energy is stored in food?", "options": ["Heat", "Light", "Chemical", "Kinetic"], "answer": "c"},
        {"question": "What is pollination?", "options": ["Fertilization", "Transfer of pollen", "Seed growth", "Watering"], "answer": "b"},
        # ... [Remaining Grade 8 questions]
    ]
}

# ----------------- QUIZ FUNCTION -----------------
def run_quiz():
    # Welcome message and prompt for grade level
    print("\nWelcome to the CBC SCIENCE QUIZ!")
    print("Select your grade level:")
    print("1. Grade 6\n2. Grade 7\n3. Grade 8\n4. All Grades Combined")

    # Get user selection
    choice = input("Enter 1, 2, 3, or 4: ")

    # Select appropriate questions based on user input
    if choice == "1":
        selected_questions = random.sample(question_bank["Grade 6"], 15)
    elif choice == "2":
        selected_questions = random.sample(question_bank["Grade 7"], 15)
    elif choice == "3":
        selected_questions = random.sample(question_bank["Grade 8"], 15)
    elif choice == "4":
        all_questions = question_bank["Grade 6"] + question_bank["Grade 7"] + question_bank["Grade 8"]
        selected_questions = random.sample(all_questions, 15)
    else:
        # Invalid choice exits the program
        print("Invalid input. Exiting.")
        return

    # Instructions for the quiz
    print("\nYou have 15 minutes total. Answer quickly! Each question has a 20-second guideline.\n")

    score = 0  # Tracks number of correct answers

    # Loop through selected questions
    for i, q in enumerate(selected_questions):
        # Display the question
        print(f"Q{i + 1}: {q['question']}")
        
        # Display the answer options (labeled a, b, c, d)
        for j, opt in enumerate(q['options']):
            print(f"  {chr(97 + j)}) {opt}")

        # Start timing the user's response
        start = time.time()

        # Get user answer
        answer = input("Your answer (a/b/c/d): ").strip().lower()

        # Calculate time taken to respond
        elapsed = time.time() - start

        # Check if answer is correct
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1  # Increase score for correct answer
        else:
            # Show the correct answer if user was wrong
            correct_option = q['options'][ord(q['answer']) - 97]
            print(f"❌ Incorrect. The correct answer was: {correct_option}\n")

        # Warn if user took too long
        if elapsed > 20:
            print("⏰ You took too long (20+ seconds). Try to be quicker!\n")

    # Calculate and show percentage score
    percentage = (score / 15) * 100
    print(f"\nYour Score: {score}/15 ({percentage:.2f}%)")

    # Display result based on performance
    if percentage >= 50:
        print("🎉 Congratulations! You passed the quiz!")
    else:
        print("💡 You did not reach the 50% pass mark. Try again!")

# ----------------- MAIN -----------------
# Entry point of the script
if __name__ == "__main__":
    run_quiz()
