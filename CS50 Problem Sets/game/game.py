import random

while True:
  try:
    level = int(input("Level: "))
    if level > 0:
       number= random.randint(1,level)
       break
    else:
        continue
  except ValueError:
     continue


while True:
  try:
    guess = int(input("Guess: "))
    if guess >= 1:
      if guess == number:
          print("Just right!")
          break
      elif guess > number:
          print("Too large!")
          continue
      else:
          print("Too small!")
          continue
    else:
        continue
  except ValueError:
     continue

