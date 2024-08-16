from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from random import randint


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x520+50+50")
        self.root.resizable(False, False)
        self.root.title("TIC_TOK_TOE")

        icon = Image.open("Image/tic_toc_toe.png")
        photo = ImageTk.PhotoImage(icon)
        self.root.iconphoto(False, photo)

        self.leftUpFrame = Frame(self.root, bd=3, relief=RIDGE)
        self.leftUpFrame.place(x=20, y=10, width=350, height=320)

        self.person1Label = Label(self.leftUpFrame, text="Person-1 Name :", font=("arial", 10, "bold"))
        self.person1Label.place(x=5, y=5)
        self.person1Entry = Entry(self.leftUpFrame, font=("arial", 10, "bold"), bg="silver", width=25)
        self.person1Entry.place(x=150, y=7)

        self.person1ImageButton = Button(self.leftUpFrame, text="Person-1 Image", command=self.img1Button,
                                         font=("arial", 10, "bold"), relief=RIDGE)
        self.person1ImageButton.place(x=5, y=50)

        self.img1Frame = Frame(self.leftUpFrame, bd=1, relief=RIDGE, bg="silver")
        self.img1Frame.place(x=150, y=47, width=180, height=100)


        self.img1Label = Label(self.img1Frame, bg="silver")
        self.img1Label.pack()

        self.person2Label = Label(self.leftUpFrame, text="Person-2 Name :", font=("arial", 10, "bold"))
        self.person2Label.place(x=5, y=152)
        self.person2Entry = Entry(self.leftUpFrame, font=("arial", 10, "bold"), bg="silver", width=25)
        self.person2Entry.place(x=150, y=155)

        self.person2ImageButton = Button(self.leftUpFrame, command=self.img2Button, text="Person-2 Image",
                                         font=("arial", 10, "bold"), relief=RIDGE)
        self.person2ImageButton.place(x=5, y=200)

        self.img2Frame = Frame(self.leftUpFrame, bd=1, relief=RIDGE, bg="silver")
        self.img2Frame.place(x=150, y=200, width=180, height=100)

        self.img2Label = Label(self.img2Frame, bg="silver")
        self.img2Label.pack()

        self.imgFrame=Frame(self.root,bd=3,relief=RIDGE,width=340,height=140)
        self.imgFrame.place(x=20, y=340)

        # Open and resize the image using PIL
        self.addPic = Image.open("Image/tic_toc_toe.png")
        self.addPic = self.addPic.resize((340, 140))

        # Convert the PIL image to a Tkinter-compatible image
        self.tk_image = ImageTk.PhotoImage(self.addPic)

        # Create a label within the imgFrame and set the image
        self.img_label = Label(self.imgFrame, image=self.tk_image)
        self.img_label.pack(expand=True, fill=BOTH)

        self.goButton = Button(self.leftUpFrame, text="GO", font=("arial", 16), bd=1, relief=RIDGE, width=8, bg="green",
                               command=self.displayInfo)
        self.goButton.place(x=5, y=260)

        self.rightFrame = Frame(self.root, bd=3, relief=RIDGE)
        self.rightFrame.place(x=390, y=10, width=580, height=480)
        self.boardFrame = Frame(self.rightFrame, bd=5, relief=RIDGE)
        self.boardFrame.place(x=10, y=100, width=550, height=272)

        # Create buttons for the Tic-Tac-Toe grid
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.boardFrame, bd=2, relief=RIDGE, bg="silver", width=10, height=2,
                                            command=lambda i=i, j=j: self.buttonClick(i, j),font=("arial",20,"bold"))
                self.buttons[i][j].grid(row=i, column=j)

        self.pic1Frame = Frame(self.rightFrame, bd=1, relief=RIDGE)
        self.pic1Frame.place(x=0, y=0, width=100, height=80)

        self.pic1 = Label(self.pic1Frame)
        self.pic1.pack()

        self.name1 = Label(self.rightFrame, text="Person-1", font=("arial", 20,"bold"))
        self.name1.place(x=200, y=10)

        self.pic2Frame = Frame(self.rightFrame, bd=1, relief=SUNKEN)
        self.pic2Frame.place(x=475, y=395, width=100, height=80)

        self.pic2 = Label(self.pic2Frame)
        self.pic2.pack()

        self.name2 = Label(self.rightFrame, text="Person-2", font=("arial", 20,"bold"))
        self.name2.place(x=200, y=420)

        self.turn = None  # Keeps track of whose turn it is
        self.board = [['' for _ in range(3)] for _ in range(3)]  # Initialize an empty board

    def img1Button(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )

        if file_path:
            self.image1 = Image.open(file_path)
            self.image1 = self.image1.resize((180, 100))

            photo = ImageTk.PhotoImage(self.image1)
            self.img1Label.config(image=photo)

            self.person1Image = photo  # Save the photo for display in the right frame

    def img2Button(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )

        if file_path:
            self.image2 = Image.open(file_path)
            self.image2 = self.image2.resize((180, 100))

            photo = ImageTk.PhotoImage(self.image2)
            self.img2Label.config(image=photo)

            self.person2Image = photo  # Save the photo for display in the right frame


    def displayInfo(self):

        if not self.person1Entry.get() or not self.person2Entry.get() or not hasattr(self, 'image1') or not hasattr(
                self, 'image2'):
            messagebox.showerror("Error", "Please ensure all fields are filled and images are selected.")
            return

        person1 = self.person1Entry.get()
        person2 = self.person2Entry.get()

        self.name1.config(text=person1)
        self.name2.config(text=person2)

        resized_image1 = self.image1.resize((100, 80))
        resized_photo1 = ImageTk.PhotoImage(resized_image1)
        self.pic1.config(image=resized_photo1)
        self.pic1.image = resized_photo1

        resized_image2 = self.image2.resize((100, 80))
        resized_photo2 = ImageTk.PhotoImage(resized_image2)
        self.pic2.config(image=resized_photo2)
        self.pic2.image = resized_photo2

        self.turn = randint(1, 2)
        if self.turn == 1:
            messagebox.showinfo("Information", f"First move goes to {person1}")
            self.currentPlayer = person1
            self.currentSymbol = "X"
        else:
            messagebox.showinfo("Information", f"First move goes to {person2}")
            self.currentPlayer = person2
            self.currentSymbol = "O"

    def buttonClick(self, i, j):
        if self.board[i][j] == "" and self.turn:
            self.board[i][j] = self.currentSymbol
            self.buttons[i][j].config(text=self.currentSymbol, state=DISABLED)

            if self.checkWin():
                messagebox.showinfo("Game Over", f"{self.currentPlayer} wins!")
                self.resetBoard()
            elif self.checkDraw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.resetBoard()
            else:
                self.switchTurn()

    def switchTurn(self):
        if self.currentSymbol == "X":
            self.currentSymbol = "O"
            self.currentPlayer = self.person2Entry.get()
        else:
            self.currentSymbol = "X"
            self.currentPlayer = self.person1Entry.get()

    def checkWin(self):
        # Check rows, columns, and diagonals for a win
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def checkDraw(self):
        # If no cells are empty and there's no winner, it's a draw
        for row in self.board:
            if "" in row:
                return False
        return True

    def resetBoard(self):
        # Reset the board for a new game
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state=NORMAL)
        self.turn = None


game = Game()
game.root.mainloop()
