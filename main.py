import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os.path


def on_closing():
    try:
        if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
            window.destroy()
    except Warning:
        return


class TrafficLight:
    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=750, height=750)
        self.canvas.pack()
        self.canvas.grid(row=0, column=0)
        self.traffic_light_obj = PhotoImage(file="TrafficLight.png")
        self.canvas.create_image(0, 0,  anchor=NW, image=self.traffic_light_obj)
        self.red_light = self.canvas.create_oval(255, 168, 300, 215, fill="gray")
        self.yellow_light = self.canvas.create_oval(255, 223, 300, 270, fill="gray")
        self.green_light = self.canvas.create_oval(255, 275, 300, 322, fill="gray")
        self.is_red = False
        self.is_yellow = False
        self.is_green = False
        self.red_timer = 16
        self.yellow_timer = 4
        self.green_timer = 16
        self.timer_label = Label(master, text="00:00", font=("Arial", 48))
        self.timer_label.place(x=200, y=400)
        self.timer = None
        self.activate_red()
    def activate_red(self):
        self.canvas.itemconfig(self.red_light, fill="red")
        self.canvas.itemconfig(self.yellow_light, fill="gray")
        self.canvas.itemconfig(self.green_light, fill="gray")
        self.is_red = True
        self.is_yellow = False
        self.is_green = False
        self.red_timer = 16
        self.update_timer()
        self.timer = self.canvas.after(16000, self.activate_yellow)

    def activate_yellow(self):
        self.canvas.itemconfig(self.red_light, fill="gray")
        self.canvas.itemconfig(self.yellow_light, fill="yellow")
        self.canvas.itemconfig(self.green_light, fill="gray")
        self.is_red = False
        self.is_yellow = True
        self.is_green = False
        self.yellow_timer = 4
        self.update_timer()
        self.timer = self.canvas.after(4000, self.activate_green)

    def activate_green(self):
        self.canvas.itemconfig(self.red_light, fill="gray")
        self.canvas.itemconfig(self.yellow_light, fill="gray")
        self.canvas.itemconfig(self.green_light, fill="green")
        self.is_red = False
        self.is_yellow = False
        self.is_green = True
        self.green_timer = 16
        self.update_timer()
        self.timer = self.canvas.after(16000, self.activate_red)

    def update_timer(self):
        if self.is_red:
            self.red_timer -= 1
            seconds = self.red_timer
            self.timer_label.config(text="{:02d}".format(seconds), fg="red", bg="#202349")
            self.timer_label.place(height=55, width=85, x=412, y=30)
            if self.red_timer == 0:
                self.red_timer = 16
                self.canvas.after_cancel(self.timer)
                self.timer = self.canvas.after(0, self.activate_yellow)
            else:
                self.timer_label.after(1000, self.update_timer)

        elif self.is_yellow:
            self.yellow_timer -= 1
            seconds = self.yellow_timer
            self.timer_label.config(text="{:02d}".format(seconds), fg="yellow", bg="#202349")
            self.timer_label.place(height=55, width=85, x=412, y=30)
            if self.yellow_timer == 0:
                self.yellow_timer = 4
                self.canvas.after_cancel(self.timer)
                self.timer = self.canvas.after(0, self.activate_green)
            else:
                self.timer_label.after(1000, self.update_timer)

        elif self.is_green:
            self.green_timer -= 1
            seconds = self.green_timer
            self.timer_label.config(text="{:02d}".format(seconds), fg="green", bg="#202349")
            self.timer_label.place(height=55, width=85, x=412, y=30)
            if self.green_timer == 0:
                self.green_timer = 16
                self.canvas.after_cancel(self.timer)
                self.timer = self.canvas.after(0, self.activate_red)
            else:
                self.timer_label.after(1000, self.update_timer)


window = tk.Tk()
window.geometry("625x625")
window.protocol("WM_DELETE_WINDOW", on_closing)
basedir = os.path.dirname(__file__)
window.iconbitmap(os.path.join(basedir, "TrafficLight.ico"))
window.title("Traffic Light")
window.resizable(width=False, height=False)
window.wm_attributes("-topmost")
traffic_light = TrafficLight(window)
window.mainloop()