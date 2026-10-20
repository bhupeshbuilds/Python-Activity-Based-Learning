key = ["A", "C", "B", "D", "A"]
answers = input("Enter 5 answers (use - for blank), separated by spaces: ").upper().split()
if len(answers) != len(key):
    print("Please enter exactly 5 answers")
else:
    correct = wrong = blank = 0
    score = 0
    for answer, correct_answer in zip(answers, key):
        if answer == "-":
            blank += 1
        elif answer == correct_answer:
            correct += 1
            score += 2
        else:
            wrong += 1
            score -= 0.5
    score = max(0, score)
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Unanswered:", blank)
    print("Final score:", score, "out of", len(key) * 2)