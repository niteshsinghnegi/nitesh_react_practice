# List of players
players = ["daks", "nitesh", "sumit"]

# List of questions
questions = [
    "1. What is the capital of India?\n(a) Delhi\n(b) Goa\n(c) Lucknow\n(d) Gujarat\n",
    "2. Who is the first Prime Minister of Bharat?\n(a) Narendra Modi\n(b) Pandit Jawaharlal Nehru\n(c) Yogi Adityanath\n(d) Lal Bahadur Shastri\n",
    "3. What is the correct chemical formula of water?\n(a) H2SO4\n(b) H2O\n(c) H2S\n(d) NaOH\n",
    "4. Which team won the Champions Trophy 2025?\n(a) India\n(b) Australia\n(c) New Zealand\n(d) South Africa\n",
    "5. What is the value of square root of 2?\n(a) 4.4143\n(b) 2.22\n(c) 4.13\n(d) 1.4142\n"
]

# List of correct answers
answers = ['a', 'b', 'b', 'a', 'd']

# Prize for each correct answer
prize_per_question = 500000

# List to store final score of each player
all_scores = []

# Game starts
for player in players:
    print(f"\n🎮 {player} starts the game!\n")
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input("Your answer (a/b/c/d): ").lower()
        if user_answer == answers[i]:
            print("✅ Your answer is right!\n")
            score += prize_per_question
        else:
            print("❌ Your answer is wrong! Game Over for you.\n")
            break
    all_scores.append(score)
    print(f"{player} earned a total of ₹{score}\n")

# Final Result
print("🎉 Game Over! Let's see who became a Crorepati:\n")

for i in range(len(players)):
    if all_scores[i] >= 10000000:
        print(f"🎉 {players[i]} became a Crorepati! Total earning ₹{all_scores[i]}")
    else:
        print(f"{players[i]} did not become a Crorepati. Total earning ₹{all_scores[i]}")
-