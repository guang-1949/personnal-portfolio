import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("地铁逃生 人数计数器")
win.geometry("320x240")
win.attributes("-topmost", True)

total_player = 32
survive = tk.IntVar(value=total_player)
my_kill = tk.IntVar(value=0)


def add_kill():
    my_kill.set(my_kill.get() + 1)
    survive.set(survive.get() - 1)

def minus_survive():
    survive.set(survive.get() - 1)

def add_survive():
    survive.set(survive.get() + 1)

def reset_game():
    survive.set(total_player)
    my_kill.set(0)

def change_total():
    global total_player
    try:
        new_num = int(input_entry.get())
        total_player = new_num
        survive.set(new_num)
        my_kill.set(0)
    except ValueError:
        pass


ttk.Label(win, text="本局存活人数", font=("SimHei",14)).pack(pady=4)
ttk.Label(win, textvariable=survive, font=("SimHei",26,"bold"), foreground="#d63031").pack()

ttk.Label(win, text="你的淘汰数", font=("SimHei",14)).pack(pady=4)
ttk.Label(win, textvariable=my_kill, font=("SimHei",20)).pack()

frame_btn = ttk.Frame(win)
frame_btn.pack(pady=10)
ttk.Button(frame_btn, text="✅ 我击杀", command=add_kill).grid(row=0, column=0, padx=3)
ttk.Button(frame_btn, text="➖ 别人减员", command=minus_survive).grid(row=0, column=1, padx=3)
ttk.Button(frame_btn, text="➕ 恢复人数", command=add_survive).grid(row=0, column=2, padx=3)
ttk.Button(frame_btn, text="🔄 重置对局", command=reset_game).grid(row=1, column=0, padx=3, pady=4)

frame_set = ttk.Frame(win)
frame_set.pack(pady=5)
ttk.Label(frame_set, text="开局人数：").grid(row=0,column=0)
input_entry = ttk.Entry(frame_set, width=6)
input_entry.insert(0, "32")
input_entry.grid(row=0,column=1)
ttk.Button(frame_set, text="确认", command=change_total).grid(row=0,column=2,padx=4)


win.mainloop()