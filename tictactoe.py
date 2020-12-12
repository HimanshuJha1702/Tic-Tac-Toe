# HIMANSHU JHA - TIC TAC TOE
# MADE ON : 8th DECEMBER, 2020
# ABOUT : A popular Tic Tac Toe game designed in Tkinter using Python supporting both Human VS Human
#         and Human VS Computer mode with added splash screen. Well Commented in order to understand clearly.


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# ADDING SPLASH SCREEN
splash_screen = Tk()
splash_screen.title("TIC TAC TOE")
# splash_screen.geometry("400x400")
splash_screen.overrideredirect(False)
# Set the splash screen path location and then comment out line no 20
my_img = ImageTk.PhotoImage(Image.open("modified_cover.png"))
splash_label = Label(image=my_img)
# my_img is the splash screen image
splash_label.pack()

global myvar

def main_window():
    global myvar
    myvar = 1
    reset()


splash_label.after(1500, main_window)


# DISABLE ALL THE BUTTONS
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# CHECK TO SEE IF SOMEONE WON
def checkifwon():
    global winner
    winner = False

    if player1_name.get() != " " and player2_name.get() != " ":

        # CHECK IF PLAYER 1 WINS
        if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
                b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
                b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
                b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
                b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
                b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
                b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
                b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
                b7['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X'):
                winner = True
                messagebox.showinfo('Tic Tac Toe', "CONGRATULATIONS! " + player1_name.get() + " Wins!!")
                disable_all_buttons()

        # CHECK IF PLAYER 2 WINS
        elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
              b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
              b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
              b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
              b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
              b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
              b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
              b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
              b7['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O'):
              winner = True
              messagebox.showinfo('Tic Tac Toe', "CONGRATULATIONS! " + player2_name.get() + " Wins!!")
              disable_all_buttons()

        # CHECK IF TIE
        elif count == 9 and winner == False:
              messagebox.showinfo("Tic Tac Toe", "It's A Tie!\nNo One Wins!")
              disable_all_buttons()

    # CHECK IF PLAYER NAME EMPTY
    else:
        messagebox.showerror("Tic Tac Toe", "Player name is empty!")


# BUTTON CLICKED FUNCTION
def b_click_human(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        if player1_name.get() != " " and player2_name.get() != " ":
            b["text"] = "X"
            clicked = False
            count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        if player1_name.get() != " " and player2_name.get() != " ":
            b["text"] = "O"
            clicked = True
            count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "This box is already occupied!")

def b_click_comp():
    pass

def mini_max():
    pass

def load_buttons(j):

    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    # b = StringVar()
    # DECLARING ALL BUTTONS
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="white",
                command=lambda: b_click_human(b9))

    # GRID OUR BUTTONS TO SCREEN
    b1.grid(row=2+j, column=0)
    b2.grid(row=2+j, column=1)
    b3.grid(row=2+j, column=2)
    b4.grid(row=3+j, column=0)
    b5.grid(row=3+j, column=1)
    b6.grid(row=3+j, column=2)
    b7.grid(row=4+j, column=0)
    b8.grid(row=4+j, column=1)
    b9.grid(row=4+j, column=2)


# START THE GAME OVER!
def reset():
    global splash_screen, root, player1_name, player2_name, clicked, count, myvar
    if (myvar == 1):
        splash_screen.destroy()
        myvar = 2
    else:
        root.destroy()
    # X starts so true
    clicked = True
    count = 0
    root = Tk()
    root.title('Ankit Singh - Tic-Tac-Toe')
    # For Creating Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # For Creating Options Menu
    options_menu = Menu(my_menu, tearoff=True)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Human v/s Human", command=reset)
    options_menu.add_command(label="Human v/s Machine", command=reset_for_comp)
    options_menu.add_separator()
    options_menu.add_command(label="Exit", command=root.quit)

    # Build our buttons
    p1 = StringVar()
    p2 = StringVar()

    player1_name = Entry(root, textvariable=p1, bd=5)
    player1_name.insert(0, " ")
    player1_name.grid(row=1, column=1, columnspan=8)
    player2_name = Entry(root, textvariable=p2, bd=5)
    player2_name.insert(0, " ")
    player2_name.grid(row=2, column=1, columnspan=8)

    label = Label(root, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=1, column=0)
    label = Label(root, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=2, column=0)

    # DECLARING ALL BUTTONS
    load_buttons(1)

def reset_for_comp():
    global root
    root.destroy()
    root = Tk()
    root.title('Ankit Singh - Tic-Tac-Toe')
    global clicked, count, b1, b2, b3, b4, b5, b6, b7, b8, b9
    clicked = True
    count = 0
    p1 = StringVar()
    player1_name = Entry(root, textvariable=p1, bd=5)
    player1_name.insert(0, " ")
    player1_name.grid(row=1, column=1, columnspan=8)
    label = Label(root, text="Player :", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=1, column=0)
    # DECLARING ALL BUTTONS
    load_buttons(0)
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # For Creating Options Menu
    options_menu = Menu(my_menu, tearoff=True)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Human v/s Human", command=reset)
    options_menu.add_command(label="Human v/s Machine", command=reset_for_comp)
    options_menu.add_separator()
    options_menu.add_command(label="Exit", command=root.quit)



mainloop()
