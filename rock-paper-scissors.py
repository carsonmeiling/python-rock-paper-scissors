import random 
import time 


lib = {1:'rock', 2: 'paper', 3: 'scissors'}

# print(compChoice)
def start():
  print("Let's play Rock Paper Scissors")
  print("Choose rock paper or scissors")
  playerChoice = input(" rock \n paper \n scissors? ")
  playerChoice = playerChoice.lower()
  compChoice = lib[random.randint(1,3)]
  time.sleep(3)
  decideWinner(compChoice,playerChoice)


def decideWinner(comp, player):
  if comp == 'rock' and player == 'rock':
    print('Tie')
  elif comp == 'rock' and player == 'scissors':
    print('Compter Wins')
  elif comp == 'rock' and player == 'paper':
    print('You win')
  elif comp == 'paper' and player == 'paper':
    print('Tie')
  elif comp == 'paper' and player == 'rock':
    print('Computer Wins')
  elif comp == 'paper' and player == 'scissors':
    print('You Win')
  elif comp == 'scissors' and player == 'scissors':
    print('Tie')
  elif comp == 'scissors' and player == 'paper':
    print('Computer Wins')
  elif comp == 'scissors' and player == 'rock':
    print('You Win')
  else:
    print('error')
  again()

def again():
  playAgain = input('Play Again: Y N')
  if playAgain == 'y' or playAgain == 'Y':
    start()
  else:
    exit()


start()