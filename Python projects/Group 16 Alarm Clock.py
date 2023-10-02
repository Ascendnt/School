import datetime
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as tkk
import time as tm
import playsound as play
import threading


class DigitalAlarmClock:
    def __init__(self, the_window):
        self.the_window = the_window
        self.the_window.title("CEIT Digital Alarm Clock")
        self.the_window.iconbitmap('alarm clock icon.ico')
        self.the_window.geometry("500x250")
        self.the_window.config(bg="green")
        self.clock = tk.Label(self.the_window, font=('Helvetica', 30, 'bold'), bg='green', fg='light blue')
        self.clock.grid(row=0, column=2)
        self.calender = tk.Label(self.the_window, font=('Helvetica', 20, 'bold'), bg="green", fg="white")
        self.calender.grid(row=1, column=2)
        self.btn = tk.Button(self.the_window, text="Set Alarm", width=12, command=self.threader)
        self.btn.grid(row=8, column=2)
        self.clock_time()
        self.alarm()

    def threader(self):
        alarm_thread = threading.Thread(target=self.set_alarm)
        alarm_thread.start()

    def set_alarm(self):
        # FORMULA TO SET ALARM
        try:
            global x, y
            if self.box.get() == "AM":
                x = int(self.entry1.get())
                y = int(self.entry2.get())
            if self.box.get() == "PM":
                x = int(self.entry1.get()) + 12
                y = int(self.entry2.get())
                showinfo("notification", "alarm has been set")
            while True:
                if x == datetime.datetime.now().hour and y == datetime.datetime.now().minute:
                    showinfo("notification", "wake up!")
                    play.playsound("alarm sound.wav")
                    break
        except:
            showerror("ERROR!", "Please enter a valid input")

    def clock_time(self):
        # WIDGET FOR CLOCK
        self.current_time = tm.strftime("%I:%M: %S %p")
        self.clock["text"] = self.current_time
        self.the_window.after(1000, self.clock_time)
        self.date = tm.strftime("%B %d, %Y")
        self.calender["text"] = self.date

    def alarm(self):
        # WIDGET FOR ALARM
        self.label1 = tk.Label(self.the_window, text="Hours:", font=('Helvetica', 15, 'bold'), bg="green", fg="white")
        self.label1.grid(row=2, column=1)
        self.entry1 = tk.Entry(self.the_window)
        self.entry1.grid(row=2, column=2)
        self.label2 = tk.Label(self.the_window, text="Minutes:", font=('Helvetica', 15, 'bold'), bg="green", fg="white")
        self.label2.grid(row=3, column=1)
        self.entry2 = tk.Entry(self.the_window)
        self.entry2.grid(row=3, column=2)
        self.box = tkk.Combobox(self.the_window, values=["AM", "PM"])
        self.box.grid(row=4, column=2)
        self.label3 = tk.Label(self.the_window, text="AM OR PM", font=('Helvetica', 15, 'bold'), bg="green", fg="white")
        self.label3.grid(row=4, column=1)


root = tk.Tk()
final = DigitalAlarmClock(root)
root.mainloop()
