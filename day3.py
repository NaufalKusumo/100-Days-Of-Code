print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height <= 120:
  print("You can't ride the rollercoaster")
else:
  if age > 18:
    bill = 12
    print("You can ride the rollercoaster and the ticket is $12")
  elif age <= 18 and age > 12:
    bill = 7
    print("You can ride the rollercoaster and the ticket is $7")
  else:
    bill = 0
    print("You are a baby, go now free")

  photo = input("Do you want a photo? Y or N")

  if photo == "Y":
    bill += 3
    print("You have to pay $3 extra")

print(f"Your total bill is ${bill}")

# Indentation sangatlah penting pada bahasa python
