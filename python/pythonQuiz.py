print("---- HELLO AND WELCOME TO PYTHON Q & A ----")

answers = ["A", "B", "C", "D"]
correctAnswers = ["A", "B", "D", "true"]
guess = []
qweries = (
  "What is not a use of python?",
  "Which file extension is used for python files?",
  "Which of the following is not a data type used in data handling with python?",
  "Arrays are similar to Lists in python, true/false?"
)

def checkAnswer(answer):
  correctGuess = False
  for ans in answers:
    if answer == ans: correctGuess = True

  if correctGuess: guess.append(answer)
  else: 
    print("Invalid Answer!")
    guess.append(" ")

print(qweries[0])
print("A. Making Cookies")
print("B. Building Powerful Applications")
print("C. Database Queries")
print("D. Ethical Hacking and Cybersecurity")
print("-------------------------------------------")
answer = input("Answer: ")
checkAnswer(answer)
print("-------------------------------------------")

print(qweries[1])
print("A. .h")
print("B. .py")
print("C. .python")
print("D. ph")
print("-------------------------------------------")
answer = input("Answer: ")
checkAnswer(answer)
print("-------------------------------------------")

print(qweries[2])
print("A. integer")
print("B. dictionary")
print("C. string")
print("D. None of the above")
print("-------------------------------------------")
answer = input("Answer: ")
checkAnswer(answer)
print("-------------------------------------------")

print(qweries[3])
print("-------------------------------------------")
answer = input("Answer: ")
if answer == "true" or answer == "false":
  guess.append(answer)
else:
  print("Invalid Answer!")
  guess.append(" ")
print("-------------------------------------------")

print(guess)
