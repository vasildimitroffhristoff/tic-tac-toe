# Global variables
board = [
  "-","-","-",
  "-","-","-",
  "-","-","-"
]

game_still_going = True
winner = None
current_player = "X"

# Init game
def displayBoard(): 
  print("\n")
  print(f'{board[0]} | {board[1]} | {board[2]}')
  print(f'{board[3]} | {board[4]} | {board[5]}')
  print(f'{board[6]} | {board[7]} | {board[8]}')
  print("\n")

def playGame():
  displayBoard()

  while game_still_going:
    handleTurn(current_player)
    checkIfGameOver()
    flipPlayer()
  
  if winner:
    print(f'Player {winner} wins.')
  else:
    print('Tie')  

def handleTurn(player):
  print(f'{player}\'s turn')
  position = input("Choose a position from 1-9: ")
  valid = False
  
  while not valid:
    while position not in map(str, list(range(1,10))):
      position = input("Wrong input!!! Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print('You can\'t go there. Go again.')

  board[position] = player
  displayBoard()

def checkIfGameOver():
  checkForWinner()
  checkIfTie()

def checkForWinner():
  global winner

  row_winner = checkRows()
  column_winner = checkColumns()
  diagonal_winner = checkDiagonals()


  if row_winner or column_winner or diagonal_winner:
    winner = current_player     
  
def checkIfTie():
  global game_still_going
  
  if "-" not in board:
    game_still_going = False

def checkRows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3: 
    game_still_going = False
  return True  
  
def checkColumns():
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3: 
    game_still_going = False
  return True  

def checkDiagonals():
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"

  if diagonal_1 or diagonal_2: 
    game_still_going = False
  return True  

def flipPlayer():
  global current_player
  current_player = 'X' if current_player == '0' else '0' 


playGame()  
