"""This is the classic Snake game from the 1990's"""
#Import section

from turtle import Screen, Turtle
from food import Food
from reptile_body import ReptileTorso
from scoreboard import Scoreboard
#from start import Start_Game
import time


#Attribution
screen = Screen()
#draw = ScreenSetup
#food = Food()

#Main Programme reptile starts here
#This is the screen setup
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Reptile_Rampage")
screen.tracer(0)

#Draws snake body, moves and steers it.
rex: ReptileTorso = ReptileTorso()
food: Food = Food()
result: Scoreboard = Scoreboard()
#begin: Start_Game = Start_Game()
t: Turtle = Turtle()

screen.listen()
screen.onkey(rex.up, "Up")
screen.onkey(rex.down, "Down")
screen.onkey(rex.left, "Left")
screen.onkey(rex.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    #begin.write_ready_to_start
    time.sleep(0.1)
    rex.move()

    #detect the food and head collisions
    if rex.segment[0].distance(food) < 15:
        food.refresh_food()
        rex.extend_snake()
        result.update_score()

    #detect wall collision
    if rex.segment[0].xcor() > +280 or rex.segment[0].xcor() < -280 or rex.segment[0].ycor() > 280 or \
    rex.segment[0].ycor() < -280:
        result.reset_score()
        rex.reset()
        # game_is_on = False #removed in lesson 182
        # result.wall_crash_gameover() # removed in lesson 182

    # *****THis section is not working******
    # detect collision with tail
    for seg in rex.segment[1:]:
       if rex.segment[0]in rex.segment[1:]:
           result.reset_score()
           rex.reset()
            # game_is_on = False # removed in lesson 182
            # result.wall_crash_gameover()

screen.exitonclick()
