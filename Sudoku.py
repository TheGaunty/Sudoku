from prettytable import PrettyTable
import random
import math
from tkinter import *
#Constants
ints = [1,2,3,4,5,6,7,8,9]
large_font = ('Verdana', 30)

##-------Build the Gui-------##
root = Tk()
root.geometry("400x400")

title = Label(root, text = "Sudoku")
title.pack(side=TOP)
gridFrame = Frame(root)
gridFrame.pack(side=TOP)
entries = []
for i in range(0,9):
    row = Frame(root)
    row.pack(side=TOP, fill=X, padx=1, pady=1)
    for j in range(0,9):
        ent = Text(row, height = 2, width = 2)
        ent.insert(END, "0")
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(ent)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
solve = Button(bottomFrame, text = "Solve Sudoku", command = (lambda e = entries: updateGrid(entries)))
solve.pack(side=BOTTOM)
#Make grid



##-------Build the Gui-------##


##-------INFO-------##
#X coord is the column number, y coord is row
#This is currently only working for puzzles that can be completed by iterating through each cell, where at least 1 cell can be solved at any time.
##-------INFO-------##

##-------Functions-------##

#Create Table
def createTable(table):
    table.clear_rows()
    for i in grid:
        table.add_row(i)
    
    print(table)
    return None

#Update Squares
def updateSquare(grid):
    squares = [[[],[],[]],[[],[],[]],[[],[],[]]]
    for i in range(0,3):
        for j in range(0,3):
            squares[0][0].append(grid[i][j])
            squares[0][1].append(grid[i][j+3])
            squares[0][2].append(grid[i][j+6])
    for i in range(3,6):
        for j in range(0,3):
            squares[1][0].append(grid[i][j])
            squares[1][1].append(grid[i][j+3])
            squares[1][2].append(grid[i][j+6])
    for i in range(6,9):
        for j in range(0,3):
            squares[2][0].append(grid[i][j])
            squares[2][1].append(grid[i][j+3])
            squares[2][2].append(grid[i][j+6])
    return squares
    
#Generate the random number
def findPossible(grid, posx, posy):
    rNum = [1,2,3,4,5,6,7,8,9]
    cNum = [1,2,3,4,5,6,7,8,9]
    sNum = [1,2,3,4,5,6,7,8,9]
    num = []
    #Check row based on x coord
    for i in grid[posx]:
        if i != 0:
            rNum.remove(i)      
    #Check column based on y coord
    for i in range(0,9):
        if grid[i][posy] != 0:
            cNum.remove(grid[i][posy])
    
    #Check Squares based on posx and posy
    squares = updateSquare(grid)
    xSqr = math.floor(posx/3)
    ySqr = math.floor(posy/3)
    for i in squares[xSqr][ySqr]:
        if i != 0:
            sNum.remove(i)

    for i in range(0,10):
        if (i in rNum) and (i in cNum) and (i in sNum):
            num.append(i)

    return num

#Check the end result
def check(grid):
    for i in range(0,9):
        for j in range(0,9):
            pos = findPossible(grid, i, j)
            if len(pos) != 0:
                return False 
    return True


#Solve the sudoku
def solveGiven(grid):
    for k in range(0,20):
        for i in range(0,9):
            for j in range(0,9):
                if grid[i][j] == 0:
                    pos = findPossible(grid, i, j)
                    if len(pos) == 1:
                        grid[i][j] = pos[0]

#Update Grid from input
def updateGrid(entires):
    for entry in entries:
        text = entry.get("1.0",END)
        print(text)

##-------Functions-------##

##-------Main-------##

grid =  [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
        ]

print(grid[0])
#Initiate table output
        
out = PrettyTable()
out.title = ''
out.field_names = []
#createTable(out)




#createTable(out)           


##-------Main-------##






