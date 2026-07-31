import random

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
        cell = document.createElement("div")
        cell.className = "cell"

        display = squares[i]

        if display == "X":
            display = "🍓"
            cell.classList.add("x")

        elif display == "O":
            display = "🍫"
            cell.classList.add("o")

        cell.innerHTML = display
        board.appendChild(cell)

        cell.addEventListener(
            "click",
            create_proxy(lambda e, index=i: make_move(index))
        )
        # event handler

# human making a move
def make_move(index):

    global current_player
    global game_over
    global x_score

    if game_over:
        return

    if current_player != "X":
        return

    if squares[index] != " ":
        return

    squares[index] = "X"
    draw_board()

    if check_win("X"):
        x_score += 1
        update_scoreboard()

        document.getElementById(
            "status"
        ).innerHTML = "🍓 You Win!"

        document.getElementById(
            "restart"
        ).innerHTML = "♡ New Round ♡"

        game_over = True
        return

    if " " not in squares:
        document.getElementById(
            "status"
        ).innerHTML = "🍦 Cat's Game!"

        document.getElementById(
            "restart"
        ).innerHTML = "♡ New Round ♡"

        game_over = True
        return

    current_player = "O"

    document.getElementById(
        "status"
    ).innerHTML = "🍫 Computer Thinking..."

    computer_move()

# ai / computer move
def computer_move():
    global current_player
    global game_over
    global o_score

    available = []

    for i in range(9):
        if squares[i] == " ":
            available.append(i)

    if len(available) == 0:
        return

    move = random.choice(available)
    squares[move] = "O"
    draw_board()

    if check_win("O"):
        o_score += 1
        update_scoreboard()

        document.getElementById(
            "status"
        ).innerHTML = "🍫 Computer Wins!"

        document.getElementById(
            "restart"
        ).innerHTML = "♡ New Round ♡"

        game_over = True
        return

    if " " not in squares:
        document.getElementById(
            "status"
        ).innerHTML = "🍦 Cat's Game!"

        document.getElementById(
            "restart"
        ).innerHTML = "♡ New Round ♡"

        game_over = True
        return

    current_player = "X"

    document.getElementById(
        "status"
    ).innerHTML = "🍓 Your Turn"

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
    ).innerHTML = "🍓 Your Turn"

    document.getElementById(
        "restart"
    ).innerHTML = "♡ Restart ♡"

# initializing the game
draw_board()
update_scoreboard()

document.getElementById(
    "status"
).innerHTML = "🍓 Your Turn"

restart_button = document.getElementById("restart")

restart_button.addEventListener(
    "click",
    create_proxy(restart_game)
)