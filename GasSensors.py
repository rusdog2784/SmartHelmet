from Tkinter import *
import time, os, sys, random

font = "Helvetica"
font_size = 18

class GasSensors(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw, width=145, height=165)
        self.g1 = 0.0
        self.g1str = StringVar()
        self.g2 = 0.0
        self.g2str = StringVar()
        self.g3 = 0.0
        self.g3str = StringVar()
        self.g4 = 0.0
        self.g4str = StringVar()
        self.makeWidgets()
        self._update()

    def makeWidgets(self):
        g1 = Label(self, textvariable=self.g1str, font=(font, font_size), anchor="e", height=2, width=14, borderwidth=1, highlightbackground="grey", relief="solid")
        g2 = Label(self, textvariable=self.g2str, font=(font, font_size), anchor="e", height=2, width=14, borderwidth=1, highlightbackground="grey", relief="solid")
        g3 = Label(self, textvariable=self.g3str, font=(font, font_size), anchor="e", height=2, width=14, borderwidth=1, highlightbackground="grey", relief="solid")
        g4 = Label(self, textvariable=self.g4str, font=(font, font_size), anchor="e", height=2, width=14, borderwidth=1, highlightbackground="grey", relief="solid")
        g1.place(x=0, y=0)
        g2.place(x=0, y=40)
        g3.place(x=0, y=80)
        g4.place(x=0, y=120)

    def _update(self):
        self._setSensors()
        rand_time = (int)(random.uniform(1.0, 3.0) * 1000)
        self._timer = self.after(rand_time, self._update)

    def _setSensors(self):
        self.g1 = self.g1 + random.uniform(0.0, 1.0)
        self.g1str.set('%02d ppm ' % (self.g1))
        self.g2 = self.g2 + random.uniform(0.0, 0.5)
        self.g2str.set('%02d ppm ' % (self.g2))
        self.g3 = self.g3 + random.uniform(0.0, 0.5)
        self.g3str.set('%02d ppm ' % (self.g3))
        self.g4 = self.g4 + random.uniform(0.0, 1.0)
        self.g4str.set('%02d ppm ' % (self.g4))