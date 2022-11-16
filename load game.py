import chess
import chess.pgn
  
# creating a virtual chessboard
board = chess.Board()
  
print(board)

pgn = open("testgame.pgn")  # opening the file in python

game = chess.pgn.read_game(pgn)  # reading the game present in file

print(game)
# username of the player playing with white
white_username = game.headers['White']
  
# username of the player playing with black
black_username = game.headers['Black']
time_control = game.headers['TimeControl'] 
  
# time format of the game
# who won the game
game_result = game.headers['Result']  
  
# Make sure that each header name
# used above is present in the PGN
print("White's chess.com Username:", white_username)
print("Black's chess.com Username:", black_username)
print("Game's Time Control:", time_control, "seconds")
print("Game Result:", game_result)
  
# If white wins: 1-0
# If black wins: 0-1
# If game drawn: 1/2-1/2

# The move number for which we want the FEN
move_number = 8
  
# Go through each move in the game until
# we reach the required move number
for number, move in enumerate(game.mainline_moves()):
      
    # It copies the move played by each 
    # player on the virtual board
    board.push(move)
      
    # Remember that number starts from 0
    if number == move_number:  
        break
  
fen = board.fen()
print(fen)
print(board)