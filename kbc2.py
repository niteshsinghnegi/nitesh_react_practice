# List of players
players = ["Amit", "Ravi", "Sita"]

# List of questions
questions = [
    "1. Capital of India?\n(a) Mumbai\n(b) Delhi\n(c) Kolkata\n(d) Chennai",
    "2. Who is the father of Computer?\n(a) Charles Babbage\n(b) Bill Gates\n(c) Newton\n(d) Einstein"
]

# List of correct answers
answers = ['b', 'a']

# Prize per correct answer
prize_per_question = 500000  # ₹5 lakh per correct answer

# List to store scores of each player
scores = []

# Quiz logic for each player
for player in players:
    print(f"\n🎮 {player} का खेल शुरू हुआ!\n")
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input("आपका जवाब (a/b/c/d): ").lower()
        if user_answer == answers[i]:
            print("✅ सही उत्तर!\n")
            score += prize_per_question
        else:
            print("❌ गलत उत्तर!\n")
            break
    scores.append(score)
    print(f"{player} ने कुल ₹{score} कमाए।\n")

# Final Result
print("🏁 खेल समाप्त! आइए देखते हैं कौन बना करोड़पति:\n")

for i in range(len(players)):
    if scores[i] >= 10000000:  # 1 Crore
        print(f"🎉 {players[i]} बना करोड़पति! कुल कमाई ₹{scores[i]}")
    else:
        print(f"{players[i]} करोड़पति नहीं बन पाए। कुल कमाई ₹{scores[i]}")
