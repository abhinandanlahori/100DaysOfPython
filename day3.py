print("press S if you wanna continue")
ifwant=input()
if ifwant == "S":
  print("Choose the room")
  room=input()
  if room == "A":
    print("You lost. Lava")
  elif room == "B":
    print("You lost. Snakes")
  elif room == "C":
    print("You won!")
  else:
    print("Bitch")
else:
  print()
