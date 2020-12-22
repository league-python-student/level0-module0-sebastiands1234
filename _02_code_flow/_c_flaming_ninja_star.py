import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

colors = ['red','blue','green','yellow','orange']

def getNextColor(i):
    return colors[i % len(colors)]

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    
    baseSize = 200;         # the size of the black part of the star
    flameSize = 130;        # the length of the flaming arms
    
    # Make a new turtle
    Sebastian = turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    Sebastian.shape('turtle')
    # Set the turtle width to 2
    Sebastian.width(2)
    # Set the turtle speed to 0 (fastest)
    Sebastian.speed(0)
    # Use a for loop to repeat all of the code below ONE time (we will change this later)
    for i in range(50):
        Sebastian.fillcolor('orange')
        Sebastian.begin_fill()
        Sebastian.right(1/8)
        Sebastian.forward(64)
        Sebastian.left(48)
        Sebastian.forward(130)
        Sebastian.right(170)
        Sebastian.forward(170)
        Sebastian.right(62)
        Sebastian.forward(200)
        Sebastian.end_fill()
        Sebastian.hideturtle()
        Sebastian.pencolor('red')

        # Set the turtle .fillcolor() to orange
        
        # Call the turtle .begin_fill() function
        
        # TURN RIGHT     Turn the turtle 1/8 of a circle (hint: 360 degrees will turn a full circle)
        
        # DRAW           Move the turtle 64 pixels
        
        # TURN LEFT      Turn the turtle 40 degrees to the LEFT. (Negative numbers will turn the turtle counter-clockwise.)
        
        # DRAW FLAME     Move the turtle the distance in the variable flameSize
        
        #                Turn the turtle to the right 170 degrees
         
        #                Move the turtle the distance in the variable flameSize (again)
         
        #  TURN RIGHT    Turn the turtle 62 degrees to the right
        
        #  DRAW          Move the turtle the distance in the variable baseSize
        
        # Call the turtle .end_fill() method
        
    # Hide your turtle so you can see the pattern.
        
    # TEST   Run the program. Check that your shape is the same as the first picture in the recipe. 
    #        This is one arm of the ninja star.

    # COLOR  Change the turtle's pen color so that the flame is a different color to the rest of the star.
    #        Run the program again. Check the second picture in the recipe.

    # LOOP   When you have one arm looking right, change your for loop to repeat 25 times.
    
    # call the turtle .done() method
    turtle.done()