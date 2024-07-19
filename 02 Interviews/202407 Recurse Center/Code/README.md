# 202407 Recurse Center

## Playgrounds

* [CracklePop's permanent link on PythonTutor](https://pythontutor.com/render.html#code=i%20%3D%201%0A%0Awhile%20i%20%3C%3D%20100%3A%0A%20%20%20%20isDivisibleBy5%20%3D%20i%20%25%205%20%3D%3D%200%0A%20%20%20%20isDivisibleBy3%20%3D%20i%20%25%203%20%3D%3D%200%0A%0A%20%20%20%20if%20isDivisibleBy5%20and%20isDivisibleBy3%3A%0A%20%20%20%20%20%20%20%20print%28%22CracklePop%22%29%0A%20%20%20%20elif%20isDivisibleBy5%3A%0A%20%20%20%20%20%20%20%20print%28%22Pop%22%29%0A%20%20%20%20elif%20isDivisibleBy3%3A%0A%20%20%20%20%20%20%20%20print%28%22Crackle%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28i%29%0A%0A%20%20%20%20i%20%2B%3D%201&cumulative=false&curInstr=776&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
* [TicTacToe's permanent link on VSCode Online](?)

## Tasks

### CracklePop

> Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3, print Crackle instead of the number. If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. You can use any language.
<!--  -->
> Don’t submit a CracklePop without testing it to make sure it works. This shows carelessness and doesn’t give us confidence that you can program.

### TicTacToe

> Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal. The program should let the players take turns to input their moves. The program should report the outcome of the game.

```py
def startGame()
def resetGame()
def takeTurn()

def printGrid()
def markGrid()
def checkGrid()

def inputOption()
def checkOption()
```

> During your interview, you will pair on adding support for a computer player to your game. You can start with random moves and make the AI smarter if you have time.

```py
# Backend
# Add level: random
# Add level: perfect
# Add dynamic: GridNum = N

levels: {
  'random': [random],
  'easy': [center, corner, side],
  'medium': [win, block, center, oppositeCorner, corner, side],
  'perfect': [win, block, fork, blockFork, center, oppositeCorner, corner, side],
}

for strategies in levels:

# Frontend
print("What mode to play: \"PvP\" or \"PvC\" ?")
print("What level of difficulty: \"random\", \"easy\", \"medium\" or \"perfect\" ?")
print("Who goes first: \"player\" or \"computer\" ?")
```

## Programs

- [x] CracklePop
- [x] TicTacToe_3_PvP
- [ ] TicTacToe_3_PvC_Random
- [ ] TicTacToe_3_PvC_Perfect
- [ ] TicTacToe_N

## To Do

- [ ] Add random computer
- [ ] Add perfect computer
- [ ] Add dynamic game
- [ ] Add automated testing
- [ ] Rewrite printed message in terminal
