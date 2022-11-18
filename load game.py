import chess
import chess.pgn
import math
from tabulate import tabulate
from array import *

def calcDist(startloc, endloc):
    p = [startloc%8 + 1, startloc//8 + 1]
    q = [endloc%8 + 1, endloc//8 + 1]
    return round(math.dist(p, q),2)

def setupDatabase(filename):
    print("DBStuff")

def findPiece(ploc):
    row=0
    for r in piece_array:
        rowloc = piece_array[row][1]
        #print(ploc, rowloc)
        if (ploc == rowloc):
            return row
        row+=1





board = chess.Board()
#print(board)
pgn = open("testgame.pgn")  # opening the file in python
game = chess.pgn.read_game(pgn)  # reading the game present in file
pgn.close()

white_ELO = game.headers["WhiteElo"]
Black_ELO = game.headers["BlackElo"]
white_username = game.headers['White']
black_username = game.headers['Black']
time_control = game.headers['TimeControl'] 
game_date = game.headers['Date'] 
game_result = game.headers['Result']
game_ending = ['Termination']

piece_array = [
    ["Ra","a1",0, "R"],
    ["Nb","b1",0, "N"],
    ["Bc","c1",0, "B"],
    ["Qd","d1",0, "Q"],
    ["Ke","e1",0, "K"],
    ["Bf","f1",0, "B"],
    ["Ng","g1",0, "N"],
    ["Rh","h1",0, "R"],
    ["Pa","a2",0, "P"],
    ["Pb","b2",0, "P"],
    ["Pc","c2",0, "P"],
    ["Pd","d2",0, "P"],
    ["Pe","e2",0, "P"],
    ["Pf","f2",0, "P"],
    ["Pg","g2",0, "P"],
    ["Ph","h2",0, "P"],
    ["ra","a8",0, "r"],
    ["nb","b8",0, "n"],
    ["bc","c8",0, "b"],
    ["qd","d8",0, "q"],
    ["ke","e8",0, "k"],
    ["bf","f8",0, "b"],
    ["ng","g8",0, "n"],
    ["rh","h8",0, "r"],
    ["pa","a7",0, "p"],
    ["pb","b7",0, "p"],
    ["pc","c7",0, "p"],
    ["pd","d7",0, "p"],
    ["pe","e7",0, "p"],
    ["pf","f7",0, "p"],
    ["pg","g7",0, "p"],
    ["ph","h7",0, "p"]
]
moveNum = 0
boardnumbers = {
    "1":"a1","2":"b1","3":"c1","4":"d1","5":"e1","6":"f1","7":"g1","8":"h1",
    "9":"a2","10":"b2","11":"c2","12":"d2","13":"e2","14":"f2","15":"g2","16":"h2",
    "17":"a3","18":"b3","19":"c3","20":"d3","21":"e3","22":"f3","23":"g3","24":"h3",
    "25":"a4","26":"b4","27":"c4","28":"d4","29":"e4","30":"f4","31":"g4","32":"h4",
    "33":"a5","34":"b5","35":"c5","36":"d5","37":"e5","38":"f5","39":"g5","40":"h5",
    "41":"a6","42":"b6","43":"c6","44":"d6","45":"e6","46":"f6","47":"g6","48":"h6",
    "49":"a7","50":"b7","51":"c7","52":"d7","53":"e7","54":"f7","55":"g7","56":"h7",
    "57":"a8","58":"b8","59":"c8","60":"d8","61":"e8","62":"f8","63":"g8","64":"h8"
}
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
    if (moveNum % 2) == 0:
        color = "white"
    else:
        color = "black" 
    
    board.push(move)
    curpieceloc = move.from_square+1
    newpieceloc = move.to_square+1
    print(curpieceloc, newpieceloc)
    curpiececoor = boardnumbers[str(curpieceloc)]
    newpiececoor = boardnumbers[str(newpieceloc)]
    print(curpiececoor, newpiececoor)
    piece_row = findPiece(curpiececoor)
    print(piece_row)
    distancemoved = calcDist(move.from_square, move.to_square)
    piecemoved = piece_array[piece_row][0]
    print(color+"\t"+str(move)+"\t"+str(distancemoved)+"\t"+str(piecemoved))
    piece_array[piece_row][1] = newpiececoor
    piece_array[piece_row][2] += distancemoved
    print(piece_array[piece_row])
    moveNum += 1
    if game.is_end():
        break
print(piece_array)
#   print(board)
# fen = board.fen()
# print(fen)
# print(board)