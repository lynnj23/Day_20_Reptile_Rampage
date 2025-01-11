from turtle import Turtle

my_turtle = Turtle()

SNAKES_STARTING_POSITION = [(-20, 0), (0, 0), (10, 0)]  # this is the primary snake body element
MOVE_DISTANCE = 20
DIRECTIONS = {"East": 0, "North": 90, "West": 180, "South": 270}


class ReptileTorso:

    def __init__(self, snake=None):
        self.snake = snake
        self.segment = []
        self.create_reptile()
        #self.segment[0]

    def create_reptile(self):
        for coord in SNAKES_STARTING_POSITION:
            self.add_segment(coord)
            # this is working - it draws three boxed next to each other

    def add_segment(self, coord):
        new_segment = Turtle()  # creates a new turtle instance
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        x, y = coord
        new_segment.goto(x, y)
        self.segment.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_reptile()
        #self.segment[0]

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if DIRECTIONS["South"] != self.segment[0].heading():  # this line is diff cos of pycharm recommended adjustment
            self.segment[0].setheading(DIRECTIONS["North"])

    def down(self):
        if self.segment[0].heading() != DIRECTIONS["North"]:
            self.segment[0].setheading(DIRECTIONS["South"])

    def right(self):
        if self.segment[0].heading() != DIRECTIONS["West"]:
            self.segment[0].setheading(DIRECTIONS["East"])

    def left(self):
        if self.segment[0].heading() != DIRECTIONS["East"]:
            self.segment[0].setheading(DIRECTIONS["West"])
