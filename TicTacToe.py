# --- GLOBAL VARIABLES ---
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

player_tracking = 0

winner = False
# ------------------------


# --- FUNCTIONS OF THE GAME ---
def display_board():
  # Displays the board to the user.

  print()
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3 ")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6 ")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9 ")
  print()


def making_move(player_variable):
  # Checks whos turn is it.

  if player_variable % 2 == 0:
    player = "X"
  else:
    player = "O"
  
  # Proceeds to ask the user to make a move.
  move = int(input(f"Select the square for {player}:"))
  
  # If the square is empty, makes the move and proceed to change player again.
  # If the square it's not empty, sends "invalid square."
  if board[move - 1] == "-":
    board[move - 1] = player
    global player_tracking
    player_tracking += 1
  else:
    print("Input a valid square.")


def win_condition_horizontal():
  # Seachs for a winner in every row.

  win = False
  
  xhorizontal1 = board[0:3].count("X")
  xhorizontal2 = board[3:6].count("X")
  xhorizontal3 = board[6:9].count("X")

  ohorizontal1 = board[0:3].count("O")
  ohorizontal2 = board[3:6].count("O")
  ohorizontal3 = board[6:9].count("O")
  
  # If there's a winner for, X sets the condition to end the game.
  if (xhorizontal1 == 3 or
      xhorizontal2 == 3 or
      xhorizontal3 == 3):
    win = True
    player = "X"
  
  # If there's a winner for O, sets the condition to end the game.
  elif (ohorizontal1 == 3 or
        ohorizontal2 == 3 or
        ohorizontal3 == 3):
    win = True
    player = "O"

  # If there's a winner, ends the game.
  if win == True:
    print(f"{player} WINS!")
    global winner
    winner = True
    return


def win_condition_vertical():
  # Checks if there's a winner in every column.

  win = False
  
  xvertical1 = board[0:7:3].count("X")
  xvertical2 = board[1:8:3].count("X")
  xvertical3 = board[2:9:3].count("X")

  overtical1 = board[0:7:3].count("O")
  overtical2 = board[1:8:3].count("O")
  overtical3 = board[2:9:3].count("O")
  
  # If there's a winner for X, sets the condition to end the game.
  if (xvertical1 == 3 or
      xvertical2 == 3 or
      xvertical3 == 3):
    win = True
    player = "X"
  
  # If there's a winner for O, sets the condition to end the game.
  elif (overtical1 == 3 or
        overtical2 == 3 or
        overtical3 == 3):
    win = True
    player = "O"

  # If there's a winner, ends the game.
  if win == True:
    print(f"{player} WINS!")
    global winner
    winner = True
    return


def win_condition_diagonal():
  # Checks for a winner in both diagonals.

  win = False
  
  xdiagonal1 = board[0:10:4].count("X")
  xdiagonal2 = board[2:8:2].count("X")

  odiagonal1 = board[0:10:4].count("O")
  odiagonal2 = board[2:8:2].count("O")

  
  # If there's a winner for X, sets the condition to end the game.
  if (xdiagonal1 == 3 or
      xdiagonal2 == 3):
    win = True
    player = "X"
  
  # If there's a winner for O, sets the condition to end the game.
  elif (odiagonal1 == 3 or
        odiagonal2 == 3):
    win = True
    player = "O"
  
  # If there's a winner, ends the game.
  if win == True:
    print(f"{player} WINS!")
    global winner
    winner = True
    return


def tie_result():
  # If there's no more empty squares, sends the Tie announcement and sets the condition to end the game.
  
  empty = board.count("-")
  
  if empty == 0:
    print("That's a tie!")
    global winner
    winner = True


def result():
  # Checks for a winner first in row then in columns, if there's none only then checks for a winner in the diagonal.
  # This is so only one win condition can be authorized, to avoid when the diagonal-column win is at the same time.
  # If none of the win conditions are authorized, proceeds to check for a tie.

  win_condition_horizontal()
  win_condition_vertical()
  if winner == False:
    win_condition_diagonal()
    tie_result()


# ----------------------------
display_board()

while winner == False:
  try:
    making_move(player_tracking)
    display_board()
    result()
  except ValueError:
    print("Input a valid square.")
  except IndexError:
    print("Input a valid square.")