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
        #print(ploc, rowloc)
        if (ploc == piece_array[row][1]):
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
    ["Ra",0,0, "R"],
    ["Nb",1,0, "N"],
    ["Bc",2,0, "B"],
    ["Qd",3,0, "Q"],
    ["Ke",4,0, "K"],
    ["Bf",5,0, "B"],
    ["Ng",6,0, "N"],
    ["Rh",7,0, "R"],
    ["Pa",8,0, "P"],
    ["Pb",9,0, "P"],
    ["Pc",10,0, "P"],
    ["Pd",11,0, "P"],
    ["Pe",12,0, "P"],
    ["Pf",13,0, "P"],
    ["Pg",14,0, "P"],
    ["Ph",15,0, "P"],
    ["ra",56,0, "r"],
    ["nb",57,0, "n"],
    ["bc",58,0, "b"],
    ["qd",59,0, "q"],
    ["ke",60,0, "k"],
    ["bf",61,0, "b"],
    ["ng",62,0, "n"],
    ["rh",63,0, "r"],
    ["pa",48,0, "p"],
    ["pb",49,0, "p"],
    ["pc",50,0, "p"],
    ["pd",51,0, "p"],
    ["pe",52,0, "p"],
    ["pf",53,0, "p"],
    ["pg",54,0, "p"],
    ["ph",55,0, "p"]
]
moveNum = 0
# Go through each move in the game until
# we reach the required move number
for number, move in enumerate(game.mainline_moves()):
    if (moveNum%2 == 0):
        color = "white"
    else:
        color = "black" 
    #print(moveNum)
    if (board.san(move)=="O-O"):
        if (color == "white"):
            #print("white castle OO")
            piece_array[4][1] = 6
            piece_array[4][2] = 2
            piece_array[7][1] = 5
            piece_array[7][2] = 2
        elif (color == "black"):
            #print("black castle OO")
            piece_array[20][1] = 62
            piece_array[20][2] = 2
            piece_array[23][1] = 61
            piece_array[23][2] = 2
    elif (board.san(move)=="O-O-O"):
        if (color == "white"):
            #print("white castle OOO")
            piece_array[4][1] = 2
            piece_array[4][2] = 2
            piece_array[0][1] = 3
            piece_array[0][2] = 3
        elif (color == "black"):
            #print("black castle OOO")
            piece_array[20][1] = 58
            piece_array[20][2] = 2
            piece_array[16][1] = 59
            piece_array[16][2] = 3
    else:
        curpieceloc = move.from_square
        newpieceloc = move.to_square
        #print(curpieceloc, newpieceloc)
        piece_row = findPiece(curpieceloc)
        #print(piece_row)
        #print(piece_array)
        distancemoved = calcDist(move.from_square, move.to_square)
        #print(distancemoved)
        piecemoved = piece_array[piece_row][0]
        #print(piecemoved)
        #print(color+"\t"+str(move)+"\t"+str(distancemoved)+"\t"+str(piecemoved))
        piece_array[piece_row][1] = newpieceloc
        piece_array[piece_row][2] += distancemoved
        #print(piece_array[piece_row])
    moveNum += 1
    if game.is_end():
        break
    board.push(move)
# for line in piece_array:
#     print(* line)
print(tabulate(piece_array, headers=["piece", "location", "Distance Moved", "group"]))
#print(board)
#   print(board)
# fen = board.fen()
# print(fen)
# print(board)