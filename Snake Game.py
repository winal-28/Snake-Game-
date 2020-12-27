import turtle
import random
import time

delay = 0.1

wn = turtle.Screen()

wn.title("Snake Game")
wn.bgcolor("Green")
wn.setup(height = 600, width = 600)
wn.tracer(0)

# head

head  = turtle.Turtle()

head.speed(0)
head.shape("square")
head.color("Black")
head.penup()
head.goto(0, 0)

head.direction = "stop"


# food

food = turtle.Turtle()

food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0, 100)

segments = []

def go_up():
    head.direction = "up"

def go_left():
    head.direction = "left"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"




def move():


    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def eat():
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)

        food.goto(x,y)

        new_segment = turtle.Turtle()

        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        for index in range(len(segments)-1, 0, -1):
            x = segment[index-1].xcor()
            y = segment[index - 1].ycor()


# keyboard bindings

    wn.listen()

    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(go_down, "s")






# main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)

    eat()



#------------------------------------------------------------------------------------------------------------------------------
wn.mainloop()