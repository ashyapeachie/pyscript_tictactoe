from js import document
from pyodide.ffi import create_proxy

# initializing game's state
squares = [' '] * 9
current_player = 'X'
game_over = False

# winning conditions
win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

# checking who the winner is
def check_win(player):
    for a, b, c in win_conditions:
        if squares[a] == squares[b] == squares[c] == player:
            return True
    return False

# the board
def draw_board(): 
    board = document.getElementById("board")
    board.innerHTML=""
    board.className="board"

    for i in range(9):
        cell=document.createElement("div")
        cell.className="cell"
        cell.id=f"cell{i}"
        cell.innerHTML=squares[i]
        board.appendChild(cell)

        cell.addEventListener(
            "click",
            create_proxy(lambda e, index=i: make_move(index))
        )
        #event handler

# making a move
def make_move(index):
    global current_player
    global game_over

    if game_over:
        return

    if squares[index]!=" ":
        return

    squares[index]=current_player
    draw_board()

    if check_win(current_player):
        document.getElementById(
            "status"
        ).innerHTML=f"{current_player} Wins!"

        game_over=True

        return

    if " " not in squares:
        document.getElementById(
            "status"
        ).innerHTML="Cat's Game!"

        game_over=True

        return

    if current_player=="X":
        current_player="O"
    else:
        current_player="X"

    document.getElementById(
        "status"
    ).innerHTML=f"{current_player}'s Turn"

# starting the game
draw_board()
document.getElementById("status").innerHTML="X's Turn"
