from Tkinter import *
import time, os, sys
import random

font = "Helvetica"
font_size = 18

class Thermal(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw, width=150, height=150)
        self.temp = 0.0
        self.tempstr = StringVar()
        self.makeWidgets()
        self._update()   

    def makeWidgets(self):                         
        """ Make the temp label. """
        l = Label(self, textvariable=self.tempstr, font=(font, font_size), anchor="e", width=7)
        self._setTemp()
        l.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self): 
        """ Update the label with elapsed time. """
        self._setTemp()
        self._timer = self.after(1000, self._update)
    
    def _setTemp(self):
        self.temp = self.temp + random.uniform(0.0, 2.0)                       #Should call the update temperature function
        d = u"\u00b0"
        self.tempstr.set('%02d%s F' % (self.temp, d))