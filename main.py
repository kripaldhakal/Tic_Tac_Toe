# git init => initialize git
# git status => if you want to check what are the status of files
# git diff => if you want to check what are the changes
# git commit -m "Your message"


import tkinter    # graphical user interface library

def set_tile(row, column):
    global current_pl

    if game_over:
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = current_pl

    if current_pl == playerO:
        current_pl = playerX
    else:
        current_pl = playerO

    label["text"] = current_pl + "'s turn"

    # Check Winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Horizontally
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
        and board[row][0]["text"] != ""):
            label.config(text = board[row][0]["text"] + " is the winner", foreground = color_yellow)
            for column in range(3):
                board[row][column].config(foreground = color_yellow, background = color_light_grey)
            game_over = True
            return

    # Vertically
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
        and board[0][column]["text"] != ""):
            label.config(text = board[0][column]["text"] + " is the winner!", foreground = color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            game_over = True
            return

    # Diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
    and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground = color_yellow, background = color_light_grey)
        game_over = True
        return

    # Anti Diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        board[0][2].config(foreground = color_yellow, background = color_light_grey)
        board[1][1].config(foreground=color_yellow, background=color_light_grey)
        board[2][0].config(foreground=color_yellow, background=color_light_grey)
        game_over = True
        return

    # tie
    if turns == 9:
        game_over = True
        label.config(text = "Tie!", foreground = color_yellow)


def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label["text"] = current_pl + "'s turn"

    for row in range(3):
        for column in range(3):
            board[row][column].config(text = "", foreground = color_blue, background = color_grey)
# Game Setup
playerX = "X"
playerO = "O"
current_pl = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue  = "#4584b6"
color_yellow  = "#ffde57"
color_grey = "#343434"
color_light_grey = "#646464"

turns = 0
game_over = False

# Window Setup
window = tkinter.Tk()  # Creates the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = current_pl + "'s turn", font = ("Consolas", 20), background = color_grey,
                      foreground = "white")

label.grid(row = 0, column = 0, columnspan=3, sticky = "we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_grey, foreground=color_blue, width=4, height=1,
                                            command = lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text = "Restart", font = ("Consolas", 20), background= color_grey,
                        foreground="white", command = new_game)

button.grid(row = 4, column = 0, columnspan = 3, sticky = "we")

frame.pack()

# center the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)- (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# Format
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()