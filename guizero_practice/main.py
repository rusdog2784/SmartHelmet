from guizero import App, Box, Text, Picture

def do_nothing():
    print("did nothing")

def createWidgets():
    # Setting up temperature widget (TOP LEFT):
    # Box
    top_left_box = Box(app, grid=[0, 0, 1, 1], layout="grid", align="top")
    top_left_box.bg = "gray"
    # Picture
    temp_icon = Picture(top_left_box, image="../Assets/Images/temp_icon.gif", grid=[0, 0, 1, 1], align="left")
    temp_icon.bg = "gray"
    # Text
    temp_space = Text(top_left_box, text=" | ", size=18, grid=[1, 0, 1, 1], align="left")
    temp_space.bg = "gray"
    temp_value = Text(top_left_box, text="0.0° F", size=18, grid=[2, 0, 2, 1], align="left")
    temp_value.bg = "gray"

    # Setting up gas widget (BOTTOM LEFT):
    # Box
    bottom_left_box = Box(app, grid=[0, 1, 1, 1], layout="grid", align="bottom")
    bottom_left_box.bg = "gray"
    # Picture
    gas_icon = Picture(bottom_left_box, image="../Assets/Images/toxic_gas_icon.gif", grid=[0, 0, 1, 2], align="left")
    gas_icon.bg = "gray"
    # Text
    gas_space_MQ4 = Text(bottom_left_box, text=" | ", size=18, grid=[1, 0, 1, 1], align="left")
    gas_space_MQ4.bg = "gray"
    gas_text_MQ4 = Text(bottom_left_box, text="CH4:", size=18, grid=[2, 0, 1, 1], align="left")
    gas_text_MQ4.bg = "gray"
    gas_value_MQ4 = Text(bottom_left_box, text="0 ppm", size=18, grid=[3, 0, 1, 1], align="left")
    gas_value_MQ4.bg = "gray"
    gas_space_MQ9 = Text(bottom_left_box, text=" | ", size=18, grid=[1, 1, 1, 1], align="left")
    gas_space_MQ9.bg = "gray"
    gas_text_MQ9 = Text(bottom_left_box, text="CO:", size=18, grid=[2, 1, 1, 1], align="left")
    gas_text_MQ9.bg = "gray"
    gas_value_MQ9 = Text(bottom_left_box, text="0 ppm", size=18, grid=[3, 1, 1, 1], align="left")
    gas_value_MQ9.bg = "gray"

    # Setting up timer widget (TOP RIGHT):
    # Box
    top_right_box = Box(app, grid=[2, 0, 1, 1], layout="grid", align="top")
    top_right_box.bg = "gray"
    # Picture
    timer_icon = Picture(top_right_box, image="../Assets/Images/stopwatch_icon.gif", grid=[0, 0, 1, 1], align="left")
    timer_icon.bg = "gray"
    # Text
    timer_space = Text(top_right_box, text=" | ", size=18, grid=[1, 0, 1, 1], align="left")
    timer_space.bg = "gray"
    timer_value = Text(top_right_box, text="0:00", size=18, grid=[2, 0, 2, 1], align="left")
    timer_value.bg = "gray"

    # Setting up thermal image widget (BOTTOM RIGHT):
    # Box
    bottom_right_box = Box(app, grid=[2, 1, 1, 1], align="bottom")
    bottom_right_box.bg = "gray"
    bottom_right_box.width = 200
    bottom_right_box.height = 175
    # Picture
    thermal_image = Picture(bottom_right_box, image="genius.gif")
    thermal_image.bg = "gray"
    thermal_image.width = 200
    thermal_image.height = 175

    # Setting up the box where the video will be played
    video_box = Box(app, grid=[1, 0, 1, 2])
    video_box.bg = "white"
    video_box.width = 1520
    video_box.height = 1040
    # Picture

if __name__ == "__main__":
    app = App(title="Smart Helmet", width=1920, height=1080, layout="grid", bg="black")
    createWidgets()
    app.display()
