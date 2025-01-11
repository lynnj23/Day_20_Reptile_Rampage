from turtle import Screen


class ScreenSetup:
    def __init__(self):
        pass

    def screen_layout(self):
        screen = Screen()
        screen.setup(600, 600)
        screen.bgcolor("black")
        screen.title("Reptile_Rampage")
        screen.tracer(0)
