##
# Japanese phrase game/quiz
import random

loop = True
MENUS = ["1) Play", "2) Reward", "3) Score", "4) Quit"]
score = 0

def game():
    quiz_data = [
        {
            "question": "What does [Arigatou / ありがとう] mean?",
            "options": ["sorry", "thank you", "good afternoon", "hello"],
            "correct_answer": 2,
        },
        {
            "question": "What does [Sensei / せんせい] mean?",
            "options": ["parents", "student", "uncle", "teacher"],
            "correct_answer": 4,
        },
        {
            "question": "How do you say hello in Japanese?",
            "options": ["sayonara", "konnichiwa", "ohayo", "hello"],
            "correct_answer": 2,
        },
        {
            "question": "How many “alphabets” does Japanese have?",
            "options": ["1", "2", "3", "4"],
            "correct_answer": 3,
        },
        {
            "question": "How do you say 'Good evening' in Japanese?",
            "options": ["おはよう (Ohayou)", "こんばんは (Konbanwa)", "さようなら (Sayonara)", "いただきます (Itadakimasu)"],
            "correct_answer": 2,
        },
        {
            "question": "How do you say 'Yes' in Japanese?",
            "options": ["いいえ (Iie)", "はい (Hai)", "こんにちは (Konnichiwa)", "さようなら (Sayonara)"],
            "correct_answer": 2,
        },
        {
            "question": "How do you say 'No' in Japanese?",
            "options": ["いいえ (Iie)", "はい (Hai)", "こんにちは (Konnichiwa)", "さようなら (Sayonara)"],
            "correct_answer": 1,
        },
        {
            "question": "How do you ask 'What's your name?' in Japanese?",
            "options": ["なんですか？ (Nandesuka?)", "お元気ですか？ (Ogenki desu ka?)", "何ですか？ (Nani desu ka?)", "お名前は何ですか？ (Onamae wa nan desu ka?)"],
            "correct_answer": 4,
        },
        {
            "question": "What is the Japanese word for 'water'?",
            "options": ["ねこ (Neko)", "いぬ (Inu)", "みず (Mizu)", "たこ (Tako)"],
            "correct_answer": 3,
        },
        {
            "question": 'Translate "花" (Hana) into English.',
            "options": ["Flower", "Sun", "Rain", "Tree"],
            "correct_answer": 1,
        },
        {
            "question": 'Translate the phrase "お誕生日おめでとうございます" (Otanjobi omedetou gozaimasu) into English.',
        "options": ["Happy birthday", "Congratulations", "Thank you very much", "Excuse me"],
            "correct_answer": 1,
        },
        {
            "question": 'How do you say "I don\'t understand" in Japanese?',
            "options": ["わかります (Wakarimasu)", "わかりません (Wakarimasen)", "すみません (Sumimasen)", "ありがとう (Arigatou)"],
            "correct_answer": 2,
        },
        {
            "question": "What does [Tomodachi / ともだち] mean?",
            "options": ["friend", "dog", "tomorrow", "Saturday"],
            "correct_answer": 1,
        },
        {
            "question": "What does [Kanpai / かんぱい] mean?",
            "options": ["food", "dinner", "cheers", "good luck"],
            "correct_answer": 3,
        }]
    return quiz_data

print("Welcome to the Japanese Phrases Game!")
print("Improve and learn basic phrases in Japanese by answering questions correctly.")
print("Gain rewards by getting high scores!\n")

while loop:
    print("\n")
    for menu in MENUS:
        print(menu)

    try:
        user_choice = int(input("\nPlease pick an option: "))
        if user_choice == 1:
            print("\nPlaying game...\n")
            round_score = 0
            deduct_points = False

            questions = game()
            random.shuffle(questions)
            round_data = questions[:5]

            for idx, question in enumerate(round_data):
                print(question["question"])
                for i, option in enumerate(question["options"], start=1):
                    print(f"{i}) {option}")

                try:
                    user_answer = int(input("Your answer (1-4): "))
                    if user_answer == question["correct_answer"]:
                        print("\nCorrect!\n")
                        round_score += idx + 1 
                        print(f"Your current score: {round_score} points")
                        if idx < 4:
                            print(f"Potential points for the next question: {round_score + idx + 2}")
                        if idx == 4 or input("Do you want to continue to the next question? (y/n): ").lower() != "y":
                            break
                    else:
                        print("\nIncorrect.\n")
                        deduct_points = True
                        break
                except ValueError:
                    print("\nInvalid input. Skipping question.\n")

                if deduct_points:
                    print("You lost all points from this round.")
                    break

            score += max(0, round_score)

            print("\nRound complete!")
            print(f"You earned {round_score} points in this round.")
            print(f"Your total score is now: {score}")

        elif user_choice == 2:
            print("Rewards earned so far:")
            if score >= 15:
                print("bronze medal 🥉 (15)")
            if score >= 30:
                print("silver medal 🥈 (30)")
            if score >= 45:
                print("gold medal 🥇 (45)")
            if score < 15:
                print("Nothing here yet... Earn more points for more rewards!")

        elif user_choice == 3:
            print(f"Your current score is: {score}")
        elif user_choice == 4:
            print("\nThank you for playing")
            loop = False
        else:
            print("Please select a valid choice")
    except ValueError:
        print("Please pick a valid option")