from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import time, os, sys
import StopWatch, Temperature, GasSensors, Thermal

font = "Helvetica"
font_size = 18
backgroundColor = '#%02x%02x%02x' % (171, 176, 186)

def temperatureButtonPressed():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

root_width = 1200
root_height = 750

root = Tk()
root.title("Python GUI")
# Make TKinter window transparent:

# Hide the root window drag bar and close button
#root.overrideredirect(True)
# Make the root window always on top
root.wm_attributes("-topmost", True)
# Turn off the window shadow
root.wm_attributes("-alpha", True)
# Set the root window background color to a transparent color
#root.config(bg='systemTransparent')

root.geometry("{}x{}".format(root_width, root_height))

#TOP LEFT WIDGETS
top_left_frame = Frame(bg=backgroundColor, height=50, width=200, borderwidth=1, highlightbackground="grey", relief="solid")
top_left_frame.place(x=10, y=10)
temperature = Temperature.Temperature(root)
temperature.place(x=50 + 20, y=20)
temperature_button = Label(top_left_frame, width=40, height=40)
temp_icon = ImageTk.PhotoImage(file="./Assets/Images/temp_icon.gif")
temperature_button.config(image=temp_icon)
temperature_button.image = temp_icon
temperature_button.place(x=5, y=1)

#TOP RIGHT WIDGETS
top_right_frame = Frame(bg=backgroundColor, bd=1, height=50, width=200, borderwidth=1, highlightbackground="grey", relief="solid")
top_right_frame.place(x=root_width - 200 - 10, y=10)
stopwatch = StopWatch.StopWatch(root)
stopwatch.place(x=root_width - 200, y=20)
stopwatch_button = Label(top_right_frame, width=40, height=40)
stopwatch_icon = ImageTk.PhotoImage(file="./Assets/Images/stopwatch_icon.gif")
stopwatch_button.config(image=stopwatch_icon)
stopwatch_button.image = stopwatch_icon
stopwatch_button.place(x=200 - 50, y=1)

#BOTTOM LEFT WIDGETS
bottom_left_frame = Frame(bg=backgroundColor, bd=1, height=175, width=200, borderwidth=1, highlightbackground="grey", relief="solid")
bottom_left_frame.place(x=10, y=root_height - 175 - 10)
gasSensors = GasSensors.GasSensors(root)
gasSensors.place(x=60, y=root_height - 175 - 5)
toxic_gas_label = Label(bottom_left_frame, width=40, height=40)
toxic_gas_icon = ImageTk.PhotoImage(file="./Assets/Images/toxic_gas_icon.gif")
toxic_gas_label.config(image=toxic_gas_icon)
toxic_gas_label.image = toxic_gas_icon
toxic_gas_label.place(x=3, y=(175 / 2) - 20)

#BOTTOM LEFT WIDGETS
bottom_right_frame = Frame(bg=backgroundColor, bd=1, height=175, width=200, borderwidth=1, highlightbackground="grey", relief="solid")
bottom_right_frame.place(x=root_width - 200 - 10, y=root_height - 175 - 10)
thermal_label = Label(bottom_right_frame, width=190, height=165)
thermal_icon = ImageTk.PhotoImage(file="./Assets/Images/thermal.gif")
thermal_label.config(image=thermal_icon)
thermal_label.image = thermal_icon
thermal_label.place(x=2, y=2)

root.mainloop()
