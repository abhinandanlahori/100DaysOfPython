import random
rps = random.randint(1,3)

print("1 for R, 2 for P and 3 for S")
ui = int(input())

if ui == 1 and rps == 1:
  print("Draw")
elif ui == 1 and rps ==2:
  print("You lose")
elif ui == 1 and rps ==3:
  print("You won bitch")
elif ui == 2 and rps == 1:
  print("won")
elif ui == 2 and rps ==2:
  print("draw")
elif ui == 2 and rps ==3:
  print("lose")
elif ui == 3 and rps == 1:
  print("lose")
elif ui == 3 and rps ==2:
  print("won")
elif ui == 3 and rps ==3:
  print("draw")
else:
  print()
