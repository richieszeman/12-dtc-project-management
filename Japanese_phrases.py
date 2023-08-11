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
            "correct_answer": 2,
        },
        {
            "question": "How do you say 'Good night' in Japanese?",
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
    for menu in MENUS:
        print(menu)

    try:
        user_choice = int(input("Please pick an option: "))
        if user_choice == 1:
            print("Playing game...")
            round_score = 0

            for question in game():
                print(question["question"])
                for i, option in enumerate(question["options"], start=1):
                    print(f"{i}) {option}")

                try:
                    user_answer = int(input("Your answer (1-4): "))
                    if user_answer == question["correct_answer"]:
                        print("Correct!\n")
                        risk_choice = input("Do you want to risk your current score for a chance to earn a higher score? (y/n): ")
                        if risk_choice.lower() == "y":
                            multiplier = random.randint(2, 4)  # Random multiplier between 2 and 4
                            round_score += multiplier
                        else:
                            round_score += 1
                    else:
                        print("Incorrect.\n")
                except ValueError:
                    print("Invalid input. Skipping question.\n")

            print("Round complete!")
            print(f"You earned {round_score} points in this round.")
            score += round_score

        elif user_choice == 2:
            print("Rewards earned so far")
        elif user_choice == 3:
            print(f"Your current score is: {score}")
        elif user_choice == 4:
            print("Thank you for playing")
            loop = False
        else:
            print("Please select a valid choice")
    except ValueError:
        print("Please pick a valid option")