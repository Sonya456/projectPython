from tkinter import *

from animals.human import Human
from direction import Direction


class App(Frame):

    world = None
    canvas = None

    def __init__(self):
        print("Window initialized!")

    def addWorld(self, _world):
        window = Tk()
        self.world = _world
        self.launchWindow(window)
        window.mainloop()

    def printBoard(self):
        self.canvas.delete("all")
        for i in range(self.world.height):
            for j in range(self.world.width):
                self.canvas.create_rectangle(30 + j * 30, 35 + i * 30, 30 + 30 * self.world.width,
                                        35 + 30 * self.world.height, fill=self.world.board[j][i].Color())
                self.canvas.create_text(45 + j * 30, 50+i*30, text=self.world.board[j][i].GetSign(), font="Plurisa")
        self.canvas.pack()

    def PrintLegend(self):
        self.canvas.pack()

    def callbackB1(self):
        self.world.NextTurn()
        self.printBoard()

    def callbackB2(self):
        self.world.Save()

    def callbackB3(self):
        self.world.Load()

    def callbackB4(self):
        self.world.PrintLog()
        print("here will be log!")

    def leftArrow(self):
        self.world.NextTurn(Direction.LEFT)
        self.printBoard()
        print("Left arrow")

    def rightArrow(self):
        self.world.NextTurn(Direction.RIGHT)
        self.printBoard()
        print("Right arrow")

    def upArrow(self):
        self.world.NextTurn(Direction.UP)
        self.printBoard()
        print("Up arrow")

    def downArrow(self):
        self.world.NextTurn(Direction.DOWN)
        self.printBoard()
        print("Down arrow")

    def SuperAbility(self, event):
        print("SuperAbility pressed")
        self.world.StartHumanAbility()

    def launchWindow(self, window):
        window.title("Lizaveta Valius, 183052 ")
        window.geometry("750x500")
        window.resizable(0, 0)


        self.canvas = Canvas(window, width=1500, height=700)
        self.PrintLegend()
        self.printBoard()
        self.addButtons(window)

    def addButtons(self, window):
        b1 = Button(window, text="Next turn", command=lambda: self.callbackB1(), height=2, width=10)
        b1.place(bordermode=OUTSIDE, height=30, width=100, x=650, y=130)

        b2 = Button(window, text="Save", command=self.callbackB2, height=2, width=10)
        b2.place(bordermode=OUTSIDE, height=30, width=100, x=650, y=30)

        b3 = Button(window, text="Load", command=self.callbackB3, height=2, width=10)
        b3.place(bordermode=OUTSIDE, height=30, width=100, x=650, y=80)

        window.bind('<Left>', lambda ev: self.leftArrow())
        window.bind('<Right>', lambda ev: self.rightArrow())
        window.bind('<Up>', lambda ev: self.upArrow())
        window.bind('<Down>', lambda ev: self.downArrow())
        window.bind('<n>', self.SuperAbility)






