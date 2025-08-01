from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx = 100 ,pady = 50, bg =YELLOW , )
window.title("Pomodoro time")
window.config()

canvas = Canvas(width= 200 , height= 224 , bg = YELLOW ,highlightthickness= 0 )
tomato_png = PhotoImage(file = "tomato.gif")

canvas.create_image(100,112,image = tomato_png )
canvas.create_text(100,135,text = "00:00" ,font= (FONT_NAME , 30 ,"bold"), fill= "white")
canvas.pack()


window.mainloop()