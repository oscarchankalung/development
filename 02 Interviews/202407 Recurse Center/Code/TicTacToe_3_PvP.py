def printGrid(grid):
    print()
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print(f"-----")
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print(f"-----")
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
    print()

def markGrid(grid, turn, option):
    marks = { 1: "X", 2: "O" }
    player = (turn - 1) % 2 + 1
    index = option - 1
    grid[index] = marks[player]
    return grid

def checkGrid(grid, option):
    horz1 = ( grid[0], grid[1], grid[2] )
    horz2 = ( grid[3], grid[4], grid[5] )
    horz3 = ( grid[6], grid[7], grid[8] )

    vert1 = ( grid[0], grid[3], grid[6] )
    vert2 = ( grid[1], grid[4], grid[7] )
    vert3 = ( grid[2], grid[5], grid[8] )

    diag1 = ( grid[0], grid[4], grid[8] )
    diag2 = ( grid[2], grid[4], grid[6] )

    checklists = {
        1: ( horz1, vert1, diag1 ),
        2: ( horz1, vert2 ),
        3: ( horz1, vert3, diag2 ),
        4: ( horz2, vert1 ),
        5: ( horz2, vert2, diag1, diag2 ),
        6: ( horz2, vert3 ),
        7: ( horz3, vert1, diag2 ),
        8: ( horz3, vert2),
        9: ( horz3, vert3, diag1 ),
    }
    checklist = checklists[option]

    for streak in checklist:
        if streak[0] == streak[1] == streak[2]:
            return True
    return False

def inputOption(turn):
    player = (turn - 1) % 2 + 1
    option = input(f"Player{player}'s option: ")
    return option

def checkOption(grid, option):
    marks = { 1: "X", 2: "O" }
    options = {
        "mode": ("PvP", "PvC"), 
        "level": ("random", "easy", "medium", "perfect"),
        "first": ("player", "computer"),
        "number": (1, 2, 3, 4, 5, 6, 7, 8, 9),
        "control": ("quit", "reset"),
    }
    invalid = "Option is invalid. Please try again."
    repeated = "Option is repeated. Please try again."

    try:
        option = int(option)
        index = option - 1
        
        if grid[index] == option:
            return option, True
        elif grid[index] in marks.values():
            return option, repeated
        else:
            return option, invalid        
    except (ValueError, IndexError):
        option = str(option)

        if option in options['control']:
            return option, False
        else:
            return option, invalid

def takeTurn(grid = [1, 2, 3, 4, 5, 6, 7, 8, 9], turn = 1):
    printGrid(grid)
    option = inputOption(turn)
    option, valid = checkOption(grid, option)
    player = (turn - 1) % 2 + 1

    if valid is True:
        grid = markGrid(grid, turn, option)
        win = checkGrid(grid, option)

        if not win and turn < 9:
            turn += 1
            takeTurn(grid, turn)
        elif not win and turn == 9:
            printGrid(grid)
            print(f"Draw!")
        elif win:
            printGrid(grid)
            print(f"Player{player} win!")
    elif valid is False:
        if option == "quit":
            print()
            print("Quiting game...")
            exit
        if option == "reset":
            print()
            print("Resetting game...")
            resetGame()
    else:
        print()
        print(valid)
        takeTurn(grid, turn)

def startGame():
    print()
    print("=================")
    print("- Tic Tac Toe 3 -")
    print("=================")
    print()
    print("Player1: X")
    print("Player2: O")
    print("Options: 1, 2, 3, 4, 5, 6, 7, 8, 9, quit, reset")
    print()
    takeTurn()

def resetGame():
    print()
    takeTurn()

startGame()
