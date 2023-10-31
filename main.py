from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
# colorhunt.co provides list of color pallets is was used to get the hex codes for the colors below
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = .5
LONG_BREAK_MIN = .5
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:00")
    label2.config(text="")
    label1.config(text="Timer", bg=YELLOW, fg=GREEN)
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label1.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label1.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        label1.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# .after is how we will set up the timer. the first argument is in milliseconds. so 1000 ms is 1 s and will call
# the function at that time. .after has an unlimited number of positional arguments to pass into the function
def count_down(count):
    # math.floor() rounds down
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # below if statement corrects time if less than 10s so it's not missing a zero. just to make it look
    # better. python is unique in that we can change variable data type on the fly. In this case we reassign from
    # and int to a str with no issues. It's called dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        label2.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
# fg= argument adds color to the foreground objects
# to get a checkmark for our app you can just do a search or go to wikipedia and copy a check mark image and
# paste it into the code
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Canvas() allows you to place images or objects on top of one another
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="0:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

#calls action() when pressed
button1 = Button(text="Start", command=start_timer, highlightthickness=0)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=reset, highlightthickness=0)
button2.grid(column=2, row=2)

label1 = Label(text="Timer", bg=YELLOW, fg=GREEN)
label1.config(font=(FONT_NAME, 30, "bold"))
label1.grid(column=1, row=0)

label2 = Label(text="", bg=YELLOW, fg=GREEN)
label2.grid(column=1, row=3)




window.mainloop()
