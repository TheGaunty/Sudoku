from prettytable import *
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
solve = Button(bottomFrame, text = "Solve Sudoku", command = (lambda e = entries: updateGrid(e)))
solve.pack(side=BOTTOM)

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
    
#Generate the possible numbers
def findPossible(grid, ints, posx, posy):
    rNum = ints.copy()
    cNum = ints.copy()
    sNum = ints.copy()
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
            pos = findPossible(grid, ints, i, j)
            if len(pos) != 0:
                return False 
    return True

#Copy Grid
def copyGrid(inGrid, outGrid):
    for i in range(len(inGrid)):
        outGrid[i] = inGrid[i]
#Solve the sudoku
def solveGiven(grid):
    tempCount = 0
    count = countEmpty(grid)
    for i in range(0,9):
        for j in range(0,9):
             if grid[i][j] == 0:
                 pos = findPossible(grid, ints, i, j)
                 if len(pos) == 1:
                     grid[i][j] = pos[0]
                 else:
                    tempCount += 1
    
    if check(tempGrid) == True:
        print("True")

    grid = tempGrid.copy()    
    return  False

#Update Grid from input
def updateGrid(entires):
    for entry in entries:
        text = entry.get("1.0",END)
        print(text)

#count the blank spaces
def countEmpty(grid):
    nonZeroCount = 0
    for i in grid:
        for j in i:
            if j == 0:
                nonZeroCount += 1
    return nonZeroCount  


##-------Functions-------##

##-------Main-------##

grid =[
        [0, 3, 0, 2, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 9, 0, 0, 4],
        [7, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 1, 8, 6, 0],
        [0, 5, 0, 4, 8, 0, 0, 9, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 6, 0, 0, 0],
        [0, 7, 5, 0, 0, 8, 1, 0, 0]
        ]


out = PrettyTable()
out.title = ''
out.field_names = []
#createTable(out)
tempGrid = grid.copy()
print(tempGrid)
while solveGiven(tempGrid) == False:
    tempGrid = grid.copy()
    print(tempGrid)
    solveGiven(tempGrid)
    


createTable(out)           


##-------Main-------##






