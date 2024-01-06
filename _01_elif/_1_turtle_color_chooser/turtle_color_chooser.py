import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
# TODO 3) say hello to Mr. Charlie
    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    bobby1545 = turtle.Turtle()
    bobby1545.pensize(10)
    for i in range(100000000000):
        turtles_awesome_colors = simpledialog.askstring(title='l', prompt='what color would like')
        if turtles_awesome_colors == 'red':
            bobby1545.pencolor('red')
            bobby1545.fillcolor('red')
        elif turtles_awesome_colors == 'green':
            bobby1545.pencolor('green')
            bobby1545.fillcolor('green')
        elif turtles_awesome_colors == 'blue':
            bobby1545.pencolor('blue')
            bobby1545.fillcolor('blue')
        elif turtles_awesome_colors == 'cyan':
            bobby1545.pencolor('cyan')
            bobby1545.fillcolor('cyan')
        elif turtles_awesome_colors == 'yellow':
            bobby1545.pencolor('yellow')
            bobby1545.fillcolor('yellow')
        elif turtles_awesome_colors == 'pink':
            bobby1545.pencolor('pink')
            bobby1545.fillcolor('pink')
        elif turtles_awesome_colors == 'purple':
            bobby1545.pencolor('purple')
            bobby1545.fillcolor('purple')
        elif turtles_awesome_colors == '':
            bobby1545.pencolor(get_random_color())
            bobby1545.fillcolor(get_random_color())
        bobby1545.shape('turtle')
        bobby1545.shapesize(30)
        bobby1545.forward(200)
        bobby1545.right(90)
        bobby1545.forward(200)
        bobby1545.right(90)
        bobby1545.forward(200)
        bobby1545.right(90)
        bobby1545.forward(200)
        bobby1545.pensize(10)

    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
