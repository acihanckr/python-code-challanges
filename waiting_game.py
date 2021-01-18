from tkinter import *
from tkinter import ttk
import random
from datetime import datetime

class main_window(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('480x640')
        self.active = False
        self.ended = False
        self.time = round(2+2*random.random(),3)
        self.label = ttk.Label(self, text = 'Your target time is '
                                '{}\n'.format(self.time) +
                                '---Press Enter to Begin---')
        self.label.config(justify=CENTER)
        self.label.pack()
        self.bind('<Return>', self.enter_hit)
        self.bind('<Escape>', self.esc_hit)

    def enter_hit(self, event):
        if self.active == False:
            self.now = datetime.now()
            self.label.config(text = f'...Press enter again after {self.time} seconds...')
            self.active = True
        elif self.ended == False:
            self.then = datetime.now()
            self.active = False
            self.ended = True
            elapsed_time = round(float((self.then - self.now).seconds) +\
                            float((self.then - self.now).microseconds//1000)/1000,3)
            output_time = round(self.time - elapsed_time,3)
            first_line = f'Elapsed time: {elapsed_time} seconds\n'
            if output_time == 0:
                message = first_line + '(Right on Target)\n ...Press Esc or Return to Restart...' 
            elif output_time < 0:
                message = first_line + \
                    f'({abs(self.time - elapsed_time)} too slow) \n ...Press Esc or Return to Restart...'
            elif output_time > 0:
                message = first_line + \
                    f'({abs(self.time - elapsed_time)} too fast) \n ...Press Esc or Return to Restart...'
            self.label.config(text = message)
        else:
            self.active = False
            self.time = round(2+2*random.random(),3)
            self.label.config(text = 'Your target time is '
                                    '{}\n'.format(self.time) +
                                    '---Press Enter to Begin---')

    def esc_hit(self, event):
        self.active = False
        self.time = round(2+2*random.random(),3)
        self.label.config(text = 'Your target time is '
                                '{}\n'.format(self.time) +
                                '---Press Enter to Begin---')

root = main_window()
root.mainloop()