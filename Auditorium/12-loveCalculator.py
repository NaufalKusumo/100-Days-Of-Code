print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
totalName = name1 + name2
totalNameLow = totalName.lower()

score1 = 0
score2 = 0
score1 += totalNameLow.count("t")
score1 += totalNameLow.count("r")
score1 += totalNameLow.count("u")
score1 += totalNameLow.count("e")

score2 += totalNameLow.count("l")
score2 += totalNameLow.count("o")
score2 += totalNameLow.count("v")
score2 += totalNameLow.count("e")

totalScore = int(str(score1) + str(score2))

if totalScore <= 10 or totalScore >= 90:
    print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore >= 40 and totalScore <= 50:
    print(f"Your score is {totalScore}, you are alright together.")
else:
    print(f"Your score is {totalScore}")
