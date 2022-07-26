import random
rps = random.randint(1,3)

print("Type 1 for Rock, 2 for Paper and 3 for Scissors")
ui = int(input())

if ui == 1 and rps == 1:
  print("You Draw. AI chose Rock")
elif ui == 1 and rps == 2:
  print("You Lose. AI chose Paper")
elif ui == 1 and rps == 3:
  print("You Won. AI chose Scissor")
elif ui == 2 and rps == 1:
  print("You Won. AI chose Rock")
elif ui == 2 and rps == 2:
  print("It is a Draw. AI chose Paper")
elif ui == 2 and rps == 3:
  print("You Lose. AI chose Scissor")
elif ui == 3 and rps == 1:
  print("You Lose. AI chose Rock")
elif ui == 3 and rps == 2:
  print("You Won. AI chose Paper")
elif ui == 3 and rps == 3:
  print("It is a Draw. AI chose Scissor")
else:
  print()

