import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    Sebastian = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    Sebastian.shape('turtle')
    # Set your turtle's speed using .speed(2)
    Sebastian.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Sebastian.color('blue')
    # Move your turtle forward using .forward(100)
    Sebastian.forward(100)
    # TEST    Did your turtle move forward?
    
    # Move your turtle left or right using .left(90) or .right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    for i in range(4):
        Sebastian.left(90)
        Sebastian.forward(100)

    # TEST    Did your turtle draw a square?
    Sebastian.penup()
    # Move your turtle to a new place on the screen using .goto(x, y)
    Sebastian.goto(90,180)
    # x=0 and y=0 is the center of the screen
    
    # Have your turtle draw a circle using .circle(radius, steps=30)
    Sebastian.pendown()
    Sebastian.begin_fill()
    Sebastian.circle(100,360,100)
    Sebastian.end_fill()
    # TEST    Did your turtle draw a circle?
    
    # Add color to your shape by adding .begin_fill() before drawing the circle

    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
