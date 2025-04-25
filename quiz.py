quiz_data = [
    { "question": "What is the capital of India?", "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
      "answer": "B"
      },
    { "question": "Which language is to write python?", "options": ["A. C", "B. Java", "C. Python", "D. English"],
     "answer": "C"
     }, 
    {"question": "What is 2+22?", "option": ["A. 3", "B. 4", "C. 5", "D. 6"],
     "answer": "B"
    },

    {"question": "Which the planet is known as the Red planet?", "option": ["A. Earth", "B. Venus", "C. Mars", "D. Jupitar"],
      "answer": "c"
         
     },

    
    { "question": "What is the boiling point of water?", "options": ["A. 90C", "B. 80C", "C. 100C", "D. 70C"], 
     "answer": "C"

    },
]


score = 0
for idx, q in enumerate(quiz_data, 1):
    print(f"\nQuestion {idx}: {q['question']}")
    for option in q['options']:
        print(option)
        user_answer = input("You answer (A/B/C/D):").strip().upper()
        if user_answer == q['answer']:
            print("✅ Correct!")
            score +=1
        else:
            print(f"❌Wrong! Correct answer: {q['answer']}")
            print(f"\n🎉 You scored {score} out of {len(quiz_data)}.")
