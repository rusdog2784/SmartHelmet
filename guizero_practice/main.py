from guizero import App, Box, Text, Picture

def do_nothing():
    print("did nothing")

def createWidgets():
    # Setting up temperature widget (TOP LEFT):
    # Box
    top_left_box = Box(app, grid=[0, 0, 1, 1], layout="grid", align="top")
    top_left_box.bg = "gray"
    top_left_box.width = 200
    top_left_box.height = 75
    # Text
    temp_label = Text(top_left_box, text="Temperature:", size=18, grid=[0, 0], align="left")
    temp_label.width = 18
    temp_value = Text(top_left_box, text="0.0° F", size=18, grid=[0, 1], align="left")
    temp_value.width = 18

    # Setting up timer widget (TOP RIGHT):
    # Box
    top_right_box = Box(app, grid=[2, 0, 1, 1], align="top")
    top_right_box.bg = "gray"
    top_right_box.width = 200
    top_right_box.height = 75
    # Text
    timer_label = Text(top_right_box, text="Timer:", size=18, grid=[0, 0], align="right")
    timer_label.width = 20
    timer_value = Text(top_right_box, text="0:00", size=18, grid=[0, 1], align="right")
    timer_value.width = 20

    # Setting up gases widget (BOTTOM LEFT):
    # Box
    bottom_left_box = Box(app, grid=[0, 2, 1, 1], align="bottom")
    bottom_left_box.bg = "gray"
    bottom_left_box.width = 200
    bottom_left_box.height = 175
    # Text
    gas_label = Text(bottom_left_box, text="Gas Readings:", size=18, grid=[0, 0], align="left")
    gas_label.width = 18
    gas_value_MQ9 = Text(bottom_left_box, text="CO: 0 ppm", size=18, grid=[0, 1], align="left")
    gas_value_MQ9.width = 18
    gas_value_MQ4 = Text(bottom_left_box, text="CH4: 0 ppm", size=18, grid=[0, 2], align="left")
    gas_value_MQ4.width = 18

    # Setting up thermal image widget (BOTTOM RIGHT):
    # Box
    bottom_right_box = Box(app, grid=[2, 2, 1, 1], align="bottom")
    bottom_right_box.bg = "gray"
    bottom_right_box.width = 200
    bottom_right_box.height = 175
    # Picture
    thermal_image = Picture(bottom_right_box, image="genius.gif")
    thermal_image.width = 200
    thermal_image.height = 175

    # Setting up the box where the video will be played
    video_box = Box(app, grid=[1, 0, 1, 3])
    video_box.bg = "white"
    video_box.width = 1520
    video_box.height = 1080
    # Picture
    video_image = Picture(video_box, image="GameOn_Indiegogo.mp4")
    video_image.width = 1520
    video_image.height = 1080

app = App(title="Smart Helmet", width=1920, height=1080, layout="grid", bg="black")
createWidgets()
app.display()