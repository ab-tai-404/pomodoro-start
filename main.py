import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#52a065"
YELLOW = "#FFFF66"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
    # ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global reps , timer
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    label_1.config(text="Timer", fg=GREEN)
    check_marks.config(text = "")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 ==0:
        count = LONG_BREAK_MIN * 60
        label_1.config(fg = RED , text = "Break")

    elif reps % 2 == 0 :
        count = SHORT_BREAK_MIN * 60
        label_1.config(fg=PINK , text ="Break" )

    else :
        count = WORK_MIN * 60
        label_1.config(fg=GREEN , text = "Work " )

    count_down(count)

def count_down(count):
    global  timer
    if count  >= 0 :
        count_min =math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10 :
            count_sec = f"0{count_sec}"
        time_format = f"{count_min}:{count_sec}"
        canvas.itemconfig(time_text,text = time_format )
        timer = window.after(1000,  count_down , count - 1)
    else :
        start_timer()
        mark = ""
        if reps % 2 == 0 :
            check_marks.config(text= "✔")
        else :
            check_marks.config(text= mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx = 100 ,pady = 50, bg =YELLOW )
window.title("Pomodoro time")

label_1 = Label(text ="Timer" , fg = GREEN , font= (FONT_NAME , 35 ,"bold") ,bg = YELLOW)
label_1.grid(column = 1, row = 0)


canvas = Canvas(width= 200 , height= 224 , bg = YELLOW ,highlightthickness= 0 )
tomato_png = PhotoImage(file = "tomato.gif")
canvas.create_image(100,112,image = tomato_png )
time_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column = 1, row = 1)

start_button = Button(text="Start" , highlightthickness= 0  , command = start_timer  )
start_button.grid(column = 0, row = 2)
reset_button = Button(text="Reset" ,highlightthickness= 0  , command= reset_time )
reset_button.grid(column = 2, row = 2)

check_marks = Label( fg = GREEN , font= (FONT_NAME , 35 ,"bold") ,bg = YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()