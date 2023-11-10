import random

print()

print("Press enter to spin.\n")

symbols = ["🐱", "🐶", "🐺"]
credits = 10

while credits > 0:
  input(f"Credits: {credits} ")

  reel1 = random.choice(symbols)
  reel2 = random.choice(symbols)
  reel3 = random.choice(symbols)

  print(f"\n{reel1} {reel2} {reel3}")

  if reel1 == reel2 and reel2 == reel3:
    credits = credits + 5
    print(f"You won 5 credits\n")
  else:
    credits = credits - 1
    print("You lost\n")
