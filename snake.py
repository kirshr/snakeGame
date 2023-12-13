from turtle import Screen, Turtle
import turtle as turtle_module
import random

turtle_module.colormode(255)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        starting_positions  = [(0,0), (-20,0), (-40,0)]
        for position in starting_positions:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle('square')
        new_segment.color(random.choice(color_list))
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) -1 , 0 , -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != 270: # Prevents the snake from moving backwards
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90: # Prevents the snake from moving backwards
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0: # Prevents the snake from moving backwards
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180: # Prevents the snake from moving backwards
            self.head.setheading(0)
