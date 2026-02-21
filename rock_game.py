# Created By: Sanjana Harichandran
# Purpose: Homework 2 - Practice using Loops to Calculate the Mean 
# Authenticity - I created this program / code on my own - This work is Authentic
# Created At: 11/05/2025
# Last Modified: 11/09/2025


# import all the required libraries
from graphics import *
import time
from random import *

# Create red circles (rocks) on the screen
def generate_rocks(num_rocks, win):
    # create empty list to stack the circles
    rocks = []
    for i in range(num_rocks):
        p = win.getMouse()
        rock = Circle(p,15)
        rock.setFill("red")
        rock.draw(win)
        # append all these circles together
        rocks.append(rock)
    # return these rocks
    return rocks

# create a list of rocks that are hit by the ball
def build_hit_list(num_rocks):
    hit_list = []
    for i in range(num_rocks):
        hit_list.append(0)
    return hit_list

# create a function to check if the ball and the rock colloided
def did_collide(ball,rock):
    ball_center = ball.getCenter()
    rock_center = rock.getCenter()
    ball_radius = ball.getRadius()
    rock_radius = rock.getRadius()
    ball_x, ball_y = ball_center.getX(), ball_center.getY()
    rock_x, rock_y = rock_center.getX(), rock_center.getY()
    dx = ball_x - rock_x
    dy = ball_y - rock_y 

    distance = ((dx**2) + (dy**2)) ** 0.5
    total_radius = ball_radius + rock_radius

    if distance <= total_radius:
        return True
    else:
        return False
    
# create a function to check if the ball hits the vertical sides of the window
def hit_vertical(ball, win):
    x = ball.getCenter().getX()
    r = ball.getRadius()
    w = win.getWidth()

    if x - r <= 0 or x + r >= w:
        return True         # true if they colloided
    else:
        return False        # else false
    
# create a function to check if the ball hits the horizontal sides of the window
def hit_horizontal(ball, win):
    y = ball.getCenter().getY()
    r = ball.getRadius()
    h = win.getHeight()

    if y - r <= 0 or y + r >= h:
        return True         # true if they colloided
    else:
        return False        # else false

# Using random library and color_rgb() to choose random colors
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    return color_rgb(r, g, b)

# Create the main function of the game
def play_game():
    # create a window named "Rock Game" with height and width (500,500) and set the background white
    win = GraphWin("Rock Game!",500,500)
    win.setBackground("pink")
    # set an intro text for the game
    intro = Text(Point(250,200),
                 "Welcome to game of Rock!\n\n" 
                 "Instructions: \n" 
                 "Click anywhere to place 5 rocks on the screen.\n" 
                 "The game will start once you finish placing your rocks \n"
                 "   and play for 30 seconds.\n" 
                 "Rocks will turn 'yellow' after 3 hits and 'green' after 6 hits.\n\n" \
                 "Click anywhere to start.")
    # draw and undraw the text
    intro.draw(win)
    intro.setSize(14)
    win.getMouse()
    intro.undraw()

    # set the number of rocks to 5 
    num_rocks = 5 
    # let rocks be set to the function generate rocks()
    rocks = generate_rocks(num_rocks,win)
    # and hits be set to the function build_hit_list()
    hits = build_hit_list(num_rocks)

    # now create a circle(Ball) that would start at some random spot and fill a random color
    ball = Circle(Point(randint(50,450),(randint(50,450))), 15)
    ball.setFill(random_color())
    ball.draw(win)

    # To move the ball in different directions(up, down, sides, diagonally) 
    dx = choice([-4, -3, 3, 4])
    dy = choice([-4, -3, 3, 4])

    # Start a timer at the begining of the game
    start_time = time.time()

    # while the game is still in the time of 30sec
    while time.time() - start_time <= 30:
        # move the ball in dx, dy directions
        ball.move(dx,dy)
        # by setting a sleep time, this determines the speed of the ball
        time.sleep(0.02)
        
        # if the ball hits the vertical walls of the window, move to opposite directions and fill the ball with random colors
        if hit_vertical(ball,win):
            dx = -dx
            ball.setFill(random_color())

        # if the ball hits the horizontal walls of the window, move to opposite directions and fill the ball with random colors
        if hit_horizontal(ball,win):
            dy = -dy
            ball.setFill(random_color())

        # Whenevr the rock and the ball touch each other, count the number of hits 
        # Also, move the ball in opposite direction and change the colour of the ball
        for i in range(num_rocks):
            if did_collide(ball,rocks[i]):
                hits[i] += 1

                ball.move(-dx, -dy)
                dx = -dx 
                dy = -dy 

                dx = choice([-4, -3, 3, 4])
                dy = choice([-4, -3, 3, 4])

                ball.setFill(random_color())

                #if the rock is hit 3 times, change the color to yellow 
                if hits[i] == 3:
                    rocks[i].setFill("yellow")
                # and if the rock is hit 6 times, change it to green
                if hits[i] == 6:
                    rocks[i].setFill("green")

    # close the game with an ending text
    end_text = Text(Point(250,350),
                    "Time's up!!\n" 
                    "Thanks for Playing!\n\n" 
                    "Click anywhere to close")
    end_text.draw(win)
    win.getMouse()
    # and close the window
    win.close()

# Run the main game
play_game() 