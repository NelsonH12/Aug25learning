# Needs user input to answer questions
# Needs to calculate user score
# Needs answer dictionary
# (from video) search through dictionary using key value pairs
# variable that tracks the score
# tell them if right or wrong and show final score

#dictionary
quiz = {
  "question1": {
    "question": "What is the capital of France?",
    "answer": "Paris"
  }, #remember your commas
  "question2": {
    "question": "Who was the third president of the United States?",
    "answer": "Jefferson"
  },
  "question3": {
    "question": "What is the capital of Germany?",
    "answer": "Berlin"
  },
  "question4": {
    "question": "What is the capital of Italy?",
    "answer": "Rome"
  },
  "question5": {
    "question": "Who invented the Polio vaccine?",
    "answer": "Salk"
  },
  "question6": {
    "question": "What is the capital of Idaho?",
    "answer": "Boise"
  },
  "question7": {
    "question": "Which state was the first state?",
    "answer": "Delaware"
  },
}

#score calculator
score = 0
#ye formioli to search through the dictionary and comp answer
for key, value in quiz.items():
  print(value["question"])
  answer = input("Answer? ")

  if answer.lower() == value["answer"].lower():
    print("Correct")
    score = score + 1
    print("Your score is: " + str(score))
    print("")

  else:
    print("Wrong!  Shame!")
    print("The correct answer is: " + value["answer"] + ", you idiot.")
    print("You're doing terribly.  Your score is: " + str(score))
    print("")

print("Your final score is: " + str(score) + " out of 7 questions")
print("Your percentage is: " +str(int(score/7 * 100)) + "%")