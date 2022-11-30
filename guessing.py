import random
user = input("Please enter your name: ")
print("Game start!")
print("----------------")
while True:

  user_list  = []
  user_list.append(user)
  while True:
    min, max = map(int, input("Please select the range ([min] [max]): ").split())
    if min < 0:
      print("min number is too small")
    elif max > 200:
      print("Max number is too largar") 
    else:
      break
  num = random.randint(min, max)
  count = 0
  i = 1
  user_min = max
  user_max = min
  while True:
    guess = int(input(f'[Round {i}] Please guess the number: '))
    if guess > user_max and guess < num:
      user_max = guess
    if guess < user_min and guess > num:
      user_min = guess
    if guess > num or guess < num:
      print(f'The range is from {user_max} to {user_min}')
    else:
      print(f"Bingo! {user}, you have tried {i} times")
      break
    i = i + 1
    print("")
    try_again = input("Would you like to try again? (yes/no)")
    if try_again == "yes" or try_again == y:
      pass
    else
    
