import google.generativeai as genai
# pip install google.generativeai
import json
# pip install json

genai.configure(api_key="AIzaSyAW3uK-PFWmUaAmQwboAm7-RGzpjQX1sEk")

def generate_quiz(topic, num_questions):
    prompt = (
        f"Generate {num_questions} multiple choice questions on the topic '{topic}'. "
        f"Each question must have 4 options labeled A, B, C, and D, and mention the correct answer as a letter. "
        f"Return the result in JSON format as a list like this:\n"
        f"[{{'question': '...', 'options': ['A. ...', 'B. ...', 'C. ...', 'D. ...'], 'answer': 'A'}}, ...]"
    )

    try:
      model = genai.GenerativeModel("gemini-2.0-flash")
      response = model.generate_content(prompt)
      content = response.text.strip("```json\n")
      quiz_data = json.loads(content)
      return quiz_data
    except Exception as e:
      print("❌ Error generating Gemini response:", e)

def run_quiz(quiz_data):
    score = 0
    for idx, q in enumerate(quiz_data, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == q['answer']:
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    print(f"\n🎉 You scored {score} out of {len(quiz_data)}.")

topic = input("Enter quiz topic: ")
num = input("Number of questions: ")

quiz = generate_quiz(topic, int(num))
if quiz:
    run_quiz(quiz)
else:
    print("⚠ Could not load quiz. Try again.")