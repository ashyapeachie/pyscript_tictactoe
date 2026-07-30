from js import document
from pyodide.ffi import create_proxy

# game's state
squares = [' '] * 9
current_player = 'X'
game_over = False

x_score = 0
o_score = 0

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

# scoreboard fuction
def update_scoreboard():
    document.getElementById(
        "x-score"
    ).innerHTML = x_score

    document.getElementById(
        "o-score"
    ).innerHTML = o_score

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
    global x_score
    global o_score

    if game_over:
        return

    if squares[index]!=" ":
        return

    squares[index]=current_player
    
    draw_board()

    # winenr function
    if check_win(current_player):
        global x_score
        global o_score

        if current_player == "X":
            x_score += 1
            winner = "🍓 Strawberry"
        else:
            o_score += 1
            winner = "🍫 Chocolate"

        update_scoreboard()

        document.getElementById(
            "status"
        ).innerHTML = f"{winner} Wins! 🎉"

        game_over = True
        return

    # draw function
    if " " not in squares:
        document.getElementById(
            "status"
        ).innerHTML = "🍦 Cat's Game!"

        game_over = True
        return

    # switching players fuction
    if current_player == "X":
        current_player = "O"
        document.getElementById(
            "status"
        ).innerHTML = "🍫 Chocolate's Turn"

    else:
        current_player = "X"
        document.getElementById(
            "status"
        ).innerHTML = "🍓 Strawberry's Turn"

# restart function
def restart_game(event=None):

    global squares
    global current_player
    global game_over

    squares = [" "] * 9

    current_player = "X"

    game_over = False

    draw_board()

    document.getElementById(
        "status"
    ).innerHTML = "🍓 Strawberry's Turn"

# starting the game
draw_board()
update_scoreboard

document.getElementById(
    "status"
).innerHTML="🍓 Strawberry's Turn"

# restarting the game
restart_button = document.getElementById("restart")

restart_button.addEventListener(
    "click",
    create_proxy(restart_game)
)