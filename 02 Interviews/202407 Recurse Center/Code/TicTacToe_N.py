turn = 1
mark1 = "X"
mark2 = "O"
inputs = {}

grid = None
gridNum = 4
gridMax = gridNum * gridNum
gridDgt = len(str(gridMax))
gridRow = "-" * (gridNum * (gridDgt + 1) - 1)
gridCol = "|"


def buildGrid():
    map = []

    for i in range(gridNum):
        row = []    
        for j in range(gridNum):
            x = i * gridNum # [0, 3, 6]
            y = j + 1       # [1, 2, 3]
            value = x + y   # [1, 2, 3] > [4, 5, 6] > [7, 8, 9]
            row.append(value)
        map.append(row)
    return map

def printGrid():
    format = "0" * gridDgt - 1 + gridDgt

    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if j < gridNum - 1: 
                print(f"{value:{format}}", end = gridCol)
            else:
                print(f"{value:{format}}")
        if i < gridNum - 1: 
            print(gridRow)

# def placeMark():
#     return

def checkGrid():
    
    def checkValues(values = []):
        if len(values) == 0:
            return False

        for i in range(1, len(values)):
            prevValue = values[i - i] # [0, 1]
            currValue = values[i]     # [1, 2]
            if prevValue != currValue:
                return False

        return True

    for i in range(gridNum):
        horzValues = []
        vertValues = []
        diagValues = []

        # [00, 01, 02]
        # [10, 11, 12]
        # [20, 21, 22]
        for j in range(gridNum):
            horzValues.append(grid[i][j]) # [00, 01, 02]
            vertValues.append(grid[j][i]) # [00, 10, 20]

            if i == 0:
                diagValues.append(grid[i+j][j]) # [00, 11, 22]
            if i == gridNum - 1:
                diagValues.append(grid[j][i-j]) # [02, 12, 20]
        
        if checkValues(horzValues):
            return True
        if checkValues(vertValues):
            return True
        if checkValues(diagValues):
            return True

    return False

# def startGame():
#     return

# def resetGame():
#     return

# def endGame():
#     return

grid = buildGrid()
printGrid()
