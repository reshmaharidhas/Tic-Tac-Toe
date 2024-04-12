#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python Desktop application using Tkinter to perform basic mathematical calculations
Author: Reshma
"""

# Importing Tkinter
import tkinter as tk

# Class containing base64 format of icon pictures to use in this application
class Icons:
    PLAY_AGAIN_IMAGE = r"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAABaUlEQVR4nO3YoUuDQRgG8OcmH4IWv6YrCq6KQ3BFbAsGkywJYjeISZPMsKhgMFmGDPSw6l9g0j9As1abFg3iY7mB8cM79957XHj6/XZ3e5/7QGuYQiC9gAyxeUeM+PFhviM20R053ACv9xKAbK6AANheAB+PE4AAYDEG7q6Bb33lELjMTIEXO4bfV8ohcFmeB+97CUAAsGbArVXw9Vw5BC7lJHi6bfh1qRwCl8VZ8O4oAQhc1pfA57MEIAA4MQ52O+DHQDkELo3p/2kHGDVkmNDtAFKQ0O0AkpBh6qV/O0AMkN/t4KGXAAQe7SA6CP7YDqKFwKU5V60dZAjy0UL6l73VUP73q34gFq6ivPeVl8anE38AJWv8zX44AKUeVp8D5U/dF81P3WbFehEtpNT+OaiWwge6lsdUjgJSDzCVRSFFwKksBmkHnsojh3Q74O2B/KLpC4k5kF5Ahti8I0b8+DDfESv/S1fdkR+NGFimnW+wfgAAAABJRU5ErkJggg=="
    RESET_IMAGE = r"iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAACXBIWXMAAAsTAAALEwEAmpwYAAACa0lEQVR4nO2XS0vjUBTH+00i1aVo3RYfG8GNCzfu1IUbxYpguxLd+QXERy2u3LjwgfopEiZgZ4aZsU2DU9BKxyr4TB9pk/9wCmbmtk1oMonOMPnDWZR7c8+Pc8859zTAcxz+Zgu8NwDvA3J+BLl3zzPeLxLuH49gdnUV5ctLfBwefnvAD93dyMzPIxeP4/b0FIXDQ1wnEsgsLEDs6cHX8XHo1SpI+d3dtwM86+/H7ckJdFWFmWit9vRk/K7k8+A7OrwHvFhaglapmIJZ6cvYmLeAdJVm0kol1F5eLAGvt7e9A6TINUqRJMjRKMTeXmPf+eQkoOstAUvZrDeAZ+EwNEVho5FIQAgGmX1CVxeKmYxlFD+NjLgPWDg+ZuF2dlruSw4OmkbvVanpaXcBqV1o5bLhoCjLEDo7TfdTIUhzcy3t28SErUpuC1CKRJgIyLGYrTzi/8ACTipXDIUcOROCQZxPTeHz6Ki7gPQ6vKp6f+84Gj/29oxz6PXxBvDx0TGgendnnHOzv+/iFW9u/rpfXYfY12cbTgyFmDTJbWy4B5iemWGLZHHRNqAcjTJnUOG5BkgR+73NKOl0U4PmLYxaEr04xiWoan0Kcg2Q7ObggL2ieLxtwMYuUDg6avvbtgGTQ0PQisUmSMGiYdNaIxwNFMmBAfcByS6WlxlnxrAQizG9kVKCck5JpdAoGjg8Hbeu1tdhptrzM6oPD6brdtLCMSDZ95WVpsnGSpQa9I0TX85H/nC4nuyUU2aiaqU9lL9O/bjyp0mKRHC1tlaHoecst7UFaXbW8ZvtKiDvsfmAvB9Bzs9B+EXC/89t5idwwi3n/8uhwgAAAABJRU5ErkJggg=="
    PLAYERX = r"iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAACXBIWXMAAAsTAAALEwEAmpwYAAADkklEQVR4nO2X20sVYRTF55SmpSUqlholVPZgooGhVL4EhVBRpBBEpmJSD6EPRVcoMyJCJJAIowv00oVunJLypZumcQpCO5SWXf6VXyw2w2TnaKlzPEHnYV6++b6ZNWvvtdYeB8fhX76ceAMgAdBJMOjEvc/4f0QSCEBGBuTmwrx5f39uzhxYtAiysmDWrBgB1Evq6+HlS/j4Ee7ehdLSP58TsAsX4MMHCIXgyBFYsCAGADduhNFROH0aamrg6VN4/hyWLBn/TEoKnD8P4TDU1UFzM3z5Avv3xwDguXPQ3e2VduVKePsW2tsNSLQz1dXw7Zt9kNpD5e3qglu3YPZsnwEePgyvX8PChZEAduyI3F9YGPkBOTnw7Jmx6juDq1ZZqQQ0KcnWUlOho8N6a/lyb29aGly5Ai9eeC2gHj51ynpRz/IdoMrT1GR9WFXlrS9dCr29VjqVX6VsaICvX61v3X3btxvbe/bYHt8B6hKAzk7o7x/L2KZNBqi21pQtlk6ehORku19UBO/fG9tz58bYqAsK4NUruHoV5s/3ytfWBp8+mQ09emT9pnvyvtu3TfX5+TOUJBs2mF0cOOCpMTMTjh0zz5PCtSYGjx833ywvn/x7pgxQoFpa4PNnqKwcf9/mzdaz6slJ9N30AepS5N24YbYRzazF4rt31rOTiUXfALogQiEr4+/3VO6BAVP5NN4xdYAq2bZtlq3RfE1lHRmBioo4ASwuhsFBaG2NPqFINFJvTw/k5c0wQPflT57Y6OWuK9J+zVjX/xR3Sp0ZAaiYO3QIhofHlm/9enjwAC5ehMWLI/N6164pKdmZkgfKOvbt80q7bJkJ4s4dU65AusoVqzJxpcvfzI/TAig7UVJcuwbp6bYmIJcuQV+fpYxiT4zt3et9gFIlGDSGf52GfAWoDFVKvHkDK1bYWiAAjY3GqDsYKD2OHrX0WLPGO796tU1DGnjdjPYVoFJBA8HWrd5aWZkBkee5I5ibv/fuwePHHmP6GA0Tisi1a30GqIdfvw43b44dPoNBuH8fsrMjz5SUwNAQnDljw4SbPkqeEyd8BqhecgFqglHfqVTh8PiNr4+ScsX6zp3GsKYZTeUHD8agxOoxJYP+Sx4+hB8/YPfuia1D3nf2LHz/bgrXT5ZULn/0HaAYWLfOhs7Ll2HLFq90E11Su/7opHzZjRIoZhN1HC4n3gBIAHQSDDpx7zMSInFix+BPJ0xlak8pwJwAAAAASUVORK5CYII="
    PLAYERO = r"iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAACXBIWXMAAAsTAAALEwEAmpwYAAACw0lEQVR4nO2Yy07bUBCG8wZnBV5yWQNrLhvgEYAV7AkBXgITe1G6KRcBKhICkUqtBElgXdwd7aJJhEr33JxlSUAiURFT/VbOkVPJ92OoKo80UoTt8aeZ88+MSTGV0b/sqdcGYAmgmmSQ/f8i6V7ppqGtIZr6MGU5fuNvrwo4sDpA+hedKmaFnAzXNEOj/tX+lwPsfdtLm982qfnUdAT72xpPDdr4ukE9Kz3xAo7vjFO1Xm17ea1Ro8Mfh5Q1spQpZizH76OLI6o36m33mnWTxnbG4gGc+TRDj78fxcsuf13SbH6WOrQOx2dwLV1I09XdlXgOMaY/TssFRObscLvfd6lT6/T9EkVXaL+03wbpN5MpP2fOXtalz0uhD/zy6XJbuf2cSU9ACILbQfkgNBxrObLPDcKJBIhWwtWKMxekrMyl3Nd310LdXi3IFRB9jhsEERWOtXyuOCfiok+GBjyvnotW4qZWFtBRCd6C0MxDAWJUPdOzFQR9ThYca3n+Im/FxjvcxqIj4Mj2iCiDeqpKB9QMTcQf3h4ODoihz23+eF464MLxgog/mZsMDoiHuCGYbMDFk0URfyI3ERwQaeeGBisbULd1CKxnkUSCwS8bsPCzIETS9aYrOCCc73oPzQcpTZq1HLHum/dW7JJZcr035Vdp2EpkAWaKGREXq1loQIwhjCMYViaMqahwiq7QTe1GjLq+d33hAeEY6NxylVxkwL3Snoi3drbmeb8nIFYirEYyFJ01siLObe3W14eVr4UVy6V9YcXyGaTciq5Y2eeGWKPvR+Wu/FjT7ZBYmdKFtKu6cQ2C4GcutpXfnkl7uWFoF+iTUDxGIhxNGMsAbyX2svrNXChAfiYhHK5uP4Z718/WQ33Mh/5wRwvSDM3xwx0TomyWLWF4tZJYAN3+9TG4Neg6vl4ckMXoCSBLMqgmZ5DcRPIHUnH5pi5xpSMAAAAASUVORK5CYII="
    TICTACTOE_IMAGE = r"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"

# Main class of Tic Tac Toe game
class TicTacToe:
    currentRound = 1
    scorePlayer1 = scorePlayer2 = 0
    player1State = True
    player2State = False
    winningLines = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"], ["00", "10", "20"], ["01", "11", "21"],
                    ["02", "12", "22"], ["00", "11", "22"], ["02", "11", "20"]]
    cellsPlayer1 = []
    cellsPlayer2 = []
    hasWinner = False
    winner = -1

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1000x550")
        self.window.resizable(0,0)
        self.window.title("Tic Tac Toe")
        self.window.config(bg="#82ccdd")
        self.winnerResult = tk.StringVar()
        self.playAgainPhoto = tk.PhotoImage(data=Icons.PLAY_AGAIN_IMAGE)
        self.resetPhoto = tk.PhotoImage(data=Icons.RESET_IMAGE)
        self.player1Icon = tk.PhotoImage(data=Icons.PLAYERX)
        self.player2Icon = tk.PhotoImage(data=Icons.PLAYERO)
        self.tictactoeIcon = tk.PhotoImage(data=Icons.TICTACTOE_IMAGE)
        self.frame = tk.Frame(self.window,bg="#82ccdd")
        self.frame.pack()
        self.frameLeft = tk.Frame(self.frame,bg="#82CCDD")
        self.frameLeft.grid(row=0,column=0,padx=10)
        self.frame1 = tk.Frame(self.frame,bg="#fad390")
        self.frame1.grid(row=0,column=1,pady=10)
        self.btn1 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell00,bg="#fad390")
        self.btn1.grid(row=0,column=0)
        self.btn2 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell01,bg="#fad390")
        self.btn2.grid(row=0,column=1)
        self.btn3 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell02,bg="#fad390")
        self.btn3.grid(row=0,column=2)
        self.btn4 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell10,bg="#fad390")
        self.btn4.grid(row=1,column=0)
        self.btn5 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell11,bg="#fad390")
        self.btn5.grid(row=1,column=1)
        self.btn6 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell12,bg="#fad390")
        self.btn6.grid(row=1,column=2)
        self.btn7 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell20,bg="#fad390")
        self.btn7.grid(row=2,column=0)
        self.btn8 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell21,bg="#fad390")
        self.btn8.grid(row=2,column=1)
        self.btn9 = tk.Button(self.frame1,width=8,height=4,font=("Helvetica",15),command=self.cell22,bg="#fad390")
        self.btn9.grid(row=2,column=2)
        self.scorePlayer1Var = tk.StringVar()
        self.scorePlayer2Var = tk.StringVar()
        self.scoreLabel1 = tk.Label(self.frameLeft,text="Player 1",font=("Times New Roman",20,"bold"),bg="#82CCDD",image=self.player1Icon,compound=tk.TOP)
        self.scoreLabel1.pack(padx=25)
        self.scoreLabel2 = tk.Label(self.frameLeft,font=("Helvetica",15),textvariable=self.scorePlayer1Var,bg="#82CCDD")
        self.scorePlayer1Var.set("Score: 0")
        self.scoreLabel2.pack(padx=25)
        self.scoreLabel3 = tk.Label(self.frameLeft,text="Player 2",font=("Times New Roman",20,"bold"),bg="#82CCDD",image=self.player2Icon,compound=tk.TOP)
        self.scoreLabel3.pack(padx=25,pady=5)
        self.scoreLabel4 = tk.Label(self.frameLeft,text="Score:",font=("Helvetica",15),textvariable=self.scorePlayer2Var,bg="#82CCDD")
        self.scorePlayer2Var.set("Score: 0")
        self.scoreLabel4.pack(padx=25)
        self.frame2 = tk.Frame(self.frame)
        self.frame2.config(bg="#82ccdd")
        self.frame2.grid(row=1,column=1)
        self.player1Label = tk.Label(self.frame2,text="Player 1",bg="blue",fg="white",font=("Times New Roman",14),image=self.player1Icon,compound=tk.LEFT)
        self.player1Label.grid(row=0,column=0,padx=20)
        self.player2Label = tk.Label(self.frame2,text="Player 2",bg="blue",fg="white",font=("Times New Roman",14),image=self.player2Icon,compound=tk.LEFT,state=tk.DISABLED)
        self.player2Label.grid(row=0,column=2,padx=20)
        self.gameResult = tk.Label(self.frame2,textvariable=self.winnerResult,font=("Times New Roman",30,"bold"),bg="#82ccdd",width=14,fg="black")
        self.gameResult.grid(row=1,column=1)
        self.playAgainButton = tk.Button(self.frame2,text="Play Again",font=("Helvetica",15),command=self.playAgain,bg="#ffa801",relief=tk.RAISED,bd=3,activebackground="#FFA801",image=self.playAgainPhoto,compound=tk.RIGHT)
        self.playAgainButton.grid(row=2,column=0,pady=10,padx=10)
        self.resetButton = tk.Button(self.frame2,text="Reset Game",font=("Helvetica",15),command=self.reset,bg="#C61F1F",fg="white",relief=tk.RAISED,bd=3,activebackground="#C61F1F",image=self.resetPhoto,compound=tk.LEFT)
        self.resetButton.grid(row=2,column=2,pady=10)
        self.window.iconphoto(True,self.tictactoeIcon)
        self.window.mainloop()

    def cell00(self):
        if self.currentRound % 2 == 1:
            self.btn1.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn1.config(state=tk.DISABLED)
            self.btn1.config(background="red")
            self.cellsPlayer1.append("00")
            self.toggleState()
        else:
            self.btn1.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn1.config(state=tk.DISABLED)
            self.btn1.config(background="green")
            self.cellsPlayer2.append("00")
            self.toggleState()

    def cell01(self):
        if self.currentRound % 2 == 1:
            self.btn2.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn2.config(state=tk.DISABLED)
            self.btn2.config(background="red")
            self.cellsPlayer1.append("01")
            self.toggleState()
        else:
            self.btn2.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn2.config(state=tk.DISABLED)
            self.btn2.config(background="green")
            self.cellsPlayer2.append("01")
            self.toggleState()

    def cell02(self):
        if self.currentRound % 2 == 1:
            self.btn3.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn3.config(state=tk.DISABLED)
            self.btn3.config(background="red")
            self.cellsPlayer1.append("02")
            self.toggleState()
        else:
            self.btn3.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn3.config(state=tk.DISABLED)
            self.btn3.config(background="green")
            self.cellsPlayer2.append("02")
            self.toggleState()

    def cell10(self):
        if self.currentRound % 2 == 1:
            self.btn4.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn4.config(state=tk.DISABLED)
            self.btn4.config(background="red")
            self.cellsPlayer1.append("10")
            self.toggleState()
        else:
            self.btn4.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn4.config(state=tk.DISABLED)
            self.btn4.config(background="green")
            self.cellsPlayer2.append("10")
            self.toggleState()

    def cell11(self):
        if self.currentRound % 2 == 1:
            self.btn5.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn5.config(state=tk.DISABLED)
            self.btn5.config(background="red")
            self.cellsPlayer1.append("11")
            self.toggleState()
        else:
            self.btn5.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn5.config(state=tk.DISABLED)
            self.btn5.config(background="green")
            self.cellsPlayer2.append("11")
            self.toggleState()

    def cell12(self):
        if self.currentRound % 2 == 1:
            self.btn6.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn6.config(state=tk.DISABLED)
            self.btn6.config(background="red")
            self.cellsPlayer1.append("12")
            self.toggleState()
        else:
            self.btn6.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn6.config(state=tk.DISABLED)
            self.btn6.config(background="green")
            self.cellsPlayer2.append("12")
            self.toggleState()

    def cell20(self):
        if self.currentRound % 2 == 1:
            self.btn7.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn7.config(state=tk.DISABLED)
            self.btn7.config(background="red")
            self.cellsPlayer1.append("20")
            self.toggleState()
        else:
            self.btn7.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn7.config(state=tk.DISABLED)
            self.btn7.config(background="green")
            self.cellsPlayer2.append("20")
            self.toggleState()

    def cell21(self):
        if self.currentRound % 2 == 1:
            self.btn8.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn8.config(state=tk.DISABLED)
            self.btn8.config(background="red")
            self.cellsPlayer1.append("21")
            self.toggleState()
        else:
            self.btn8.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn8.config(state=tk.DISABLED)
            self.btn8.config(background="green")
            self.cellsPlayer2.append("21")
            self.toggleState()

    def cell22(self):
        if self.currentRound % 2 == 1:
            self.btn9.config(text="X", font=("Helvetica", 15), disabledforeground="black")
            self.btn9.config(state=tk.DISABLED)
            self.btn9.config(background="red")
            self.cellsPlayer1.append("22")
            self.toggleState()
        else:
            self.btn9.config(text="O", font=("Helvetica", 15), disabledforeground="black")
            self.btn9.config(state=tk.DISABLED)
            self.btn9.config(background="green")
            self.cellsPlayer2.append("22")
            self.toggleState()

    def toggleState(self):
        global player1State, player2State, currentRound
        if self.player1State == True:
            self.player1Label.config(state=tk.DISABLED)
            self.player2Label.config(state=tk.NORMAL)
            self.player1State = False
            self.player2State = True
        elif self.player2State == True:
            self.player2Label.config(state=tk.DISABLED)
            self.player1Label.config(state=tk.NORMAL)
            self.player1State = True
            self.player2State = False
        self.currentRound += 1
        self.analyse()

    def analyse(self):
        global hasWinner, winner, scorePlayer1, scorePlayer2
        if self.currentRound >= 6 and self.hasWinner == False:
            for element in self.winningLines:
                if set(element).issubset(self.cellsPlayer1):
                    self.hasWinner = True
                    self.winner = 1
                    self.incrementScorePlayer1()
                    break
                elif set(element).issubset(self.cellsPlayer2):
                    self.hasWinner = True
                    self.winner = 2
                    self.incrementScorePlayer2()
                    break
        if self.currentRound == 10 and self.hasWinner == False:
            self.scorePlayer1Var.set("Score: " + str(self.scorePlayer1))
            self.scorePlayer2Var.set("Score: " + str(self.scorePlayer2))
            self.winnerResult.set("Tie")
        if self.hasWinner == True:
            won = "Winner is Player " + str(self.winner)
            self.scorePlayer1Var.set("Score: " + str(self.scorePlayer1))
            self.scorePlayer2Var.set("Score: " + str(self.scorePlayer2))
            self.winnerResult.set(won)
            self.btn1.config(state=tk.DISABLED)
            self.btn2.config(state=tk.DISABLED)
            self.btn3.config(state=tk.DISABLED)
            self.btn4.config(state=tk.DISABLED)
            self.btn5.config(state=tk.DISABLED)
            self.btn6.config(state=tk.DISABLED)
            self.btn7.config(state=tk.DISABLED)
            self.btn8.config(state=tk.DISABLED)
            self.btn9.config(state=tk.DISABLED)

    def playAgain(self):
        global currentRound, cellsPlayer2, cellsPlayer2, hasWinner, winner
        self.currentRound = 1
        self.hasWinner = False
        self.winner = -1
        self.cellsPlayer1.clear()
        self.cellsPlayer2.clear()
        self.player1Label.config(state=tk.NORMAL)
        self.player2Label.config(state=tk.DISABLED)
        self.btn1.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.btn2.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.btn3.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.btn4.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.btn5.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.btn6.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.btn7.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.btn8.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.btn9.config(state=tk.NORMAL, text="", bg="#fad390",bd=1)
        self.winnerResult.set("")

    def reset(self):
        global scorePlayer1, scorePlayer2
        self.playAgain()
        self.scorePlayer1 = self.scorePlayer2 = 0
        self.scorePlayer1Var.set("Score: " + str(self.scorePlayer1))
        self.scorePlayer2Var.set("Score: " + str(self.scorePlayer2))

    def incrementScorePlayer1(self):
        global scorePlayer1
        self.scorePlayer1 += 1

    def incrementScorePlayer2(self):
        global scorePlayer2
        self.scorePlayer2 += 1
      
#object created for the class 'TicTacToe'
TicTacToe()
