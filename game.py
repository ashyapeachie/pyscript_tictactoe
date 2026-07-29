from js import document
from pyodide import create_proxy

# initializing game's state
squares = [' '] * 9
players = 'XO'

# winning conditions
win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def check_win(player):
    for a, b, c in win_conditions:
        if squares[a] == squares[b] == squares[c] == player:
            return True
    return False

def update_board():
    board_html = """
    <div class="board">
        <div class="row">
            <div class="cell" onclick="make_move(0)">{}</div>
            <div class="cell" onclick="make_move(1)">{}</div>
            <div class="cell" onclick="make_move(2)">{}</div>
        </div>

        <div class="row">
            <div class="cell" onclick="make_move(3)">{}</div>
            <div class="cell" onclick="make_move(4)">{}</div>
            <div class="cell" onclick="make_move(5)">{}</div>
        </div>

        <div class="row">
            <div class="cell" onclick="make_move(6)">{}</div>
            <div class="cell" onclick="make_move(7)">{}</div>
            <div class="cell" onclick="make_move(8)">{}</div>
        </div>
    </div>
    """.format(*squares)
    board_element = document.getElementById("board")
    board_element.innerHTML = board_html

def make_move(move):
    global players
    if squares[move] == ' ':
        squares[move] = players 
        if check_win(players):
            update_board()
            document.getElementById("status").innerHTML = f'<b>{players} wins!</b>'
            return
        if ' ' not in squares:
            update_board()
            document.getElementById("status").innerHTML = '<b>Cat\'s game!</b>'
            return
        players = players[::-1]  # switch players
        document.getElementById("status").innerHTML = f'<b>{players}\'s turn</b>'
        update_board()

# initialize the game
update_board()
document.getElementById("status").innerHTML = f'<b>{players}\'s turn</b>'
