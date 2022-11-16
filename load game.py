import chess
import chess.pgn
import math
from tabulate import tabulate

def calcDist(startloc, endloc):
    # x1 = startloc%8 + 1
    # y1 = startloc//8 + 1
    # x2 = endloc%8 + 1
    # y2 = endloc//8 + 1
    p = [startloc%8 + 1, startloc//8 + 1]
    q = [endloc%8 + 1, endloc//8 + 1]

    return round(math.dist(p, q),2)

board = chess.Board()

pgn = open("testgame.pgn")  # opening the file in python
game = chess.pgn.read_game(pgn)  # reading the game present in file

#print(game)
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
moveNum = 0
gameMoveData = {
    "P":0,
    "R":0,
    "N":0,
    "B":0,
    "Q":0,
    "K":0,
    "p":0,
    "r":0,
    "n":0,
    "b":0,
    "q":0,
    "k":0,
}
# Go through each move in the game until
# we reach the required move number
for number, move in enumerate(game.mainline_moves()):
      
    # It copies the move played by each 
    # player on the virtual board
    # print(board)
    board.push(move)
    curPiece = str(board.piece_at(move.to_square))
    if (moveNum % 2) == 0:
        color = "white"
    else:
        color = "black"
    # print(color+"\t"+ move, move.from_square, move.to_square, calcDist(move.from_square, move.to_square), board.piece_at(move.to_square))
    print(color+"\t"+str(move)+"\t"+str(calcDist(move.from_square, move.to_square))+"\t"+str(board.piece_at(move.to_square)))
    curDist = gameMoveData[curPiece] + calcDist(move.from_square, move.to_square)
    gameMoveData.update({curPiece: round(curDist,2)})
    moveNum += 1
    # Remember that number starts from 0
    if game.is_end():
        break
print(gameMoveData)
print(board)
# fen = board.fen()
# print(fen)
# print(board)