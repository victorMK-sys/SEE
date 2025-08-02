print("---- HELLO AND WELCOME TO PYTHON Q & A ----")

answers = ("A", "B", "C", "D")
correctanswers = ("A", "B", "D", "true")
qweries = (
  "Which of the following is not an ethical way to use python?",
  "Which file extension is used for python files?",
  "Which of the following is not a data type used in data handling with python?",
  "Lists are immutable in python, true/false?"
)
guesses = []
score = 0
count = 0

def checkAnswer(answer):
  if answer.upper() in answers:
    guesses.append(answer.upper())
  else:
    print("Invalid Answer!")
    guesses.append(" ")
  
def calcScore():
  global count
  global score
  if guesses[count] == correctanswers[count]: 
    print('Correct')
    score += 1
  else:
    print("Incorrect")
    print(f"Correct answer was: {correctanswers[count]}")
  count += 1


print(qweries[0])
print("A. Hacking friends devices")
print("B. Building Powerful Applications")
print("C. Database Queries")
print("D. Ethical Hacking and Cybersecurity")
print("-------------------------------------------")
answer = input("Answer: ")
checkAnswer(answer)
calcScore()
print("-------------------------------------------")

print(qweries[1])
print("A. .h")
print("B. .py")
print("C. .python")
print("D. ph")
print("-------------------------------------------")
answer = input("Answer: ")
checkAnswer(answer)
calcScore()
print("-------------------------------------------")

print(qweries[2])
print("A. integer")
print("B. dictionary")
print("C. string")
print("D. None of the above")
print("-------------------------------------------")
answer = input("Answer: ")
checkAnswer(answer)
calcScore()
print("-------------------------------------------")

print(qweries[3])
print("-------------------------------------------")
answer = input("Answer: ")
if answer == "true" or answer == "false":
  guesses.append(answer)
  calcScore()
else:
  print("Invalid answer!")
print("-------------------------------------------")

def formatArr(arr):
  for el in arr:
    print(el, end=" ")

print("Correct Answers:")
formatArr(correctanswers)
print()
print("And here is what you thought was correct:")
formatArr(guesses)
print()
print(f"Score: {score/len(qweries) * 100:.2f}%")

if score >= 3:
  print("Are you sure you never used AI? 👀")
if score <= 1:
  print("Go read some python!! 😑")