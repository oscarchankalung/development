turn = 1
mark1 = "X"
mark2 = "O"
inputs = {}

grid = None
gridNum = 3
gridCol = "|"
gridRow = "-" * (gridNum * 2 - 1)


def buildGrid():
    # [ [1,2,3], [4,5,6], [7,8,9] ]
    map = []

    for i in range(gridNum):
        row = []    
        for j in range(gridNum):
            x = i * gridNum # 0,3,6
            y = j + 1       # 1,2,3
            value = x + y
            row.append(value)
        map.append(row)
    return map

def printGrid():
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if j < gridNum - 1: 
                print(value, end = gridCol)
            else:
                print(value)
        if i < gridNum - 1: 
            print(gridRow)

# def placeMark():
#     return

# def checkGrid():
#     return

# def startGame():
#     return

# def resetGame():
#     return

# def endGame():
#     return

grid = buildGrid()
printGrid()
