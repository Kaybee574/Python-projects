#Purpose:A program that uses a turtle to create an optical illusion
#Date:10/05/2024
#Author:g24m5008

import turtle

def draw_square(t, size, color):
    """A function that draws a square of a given color(black and white) """
    t.color(color)
    for side in range(4):
        t.forward(size)
        t.left(90)

def draw_rings(t, num_squares):
    """A functions that draws 5 rings with alternating colors(black and white)"""
    for ring in range(5):
        if ring % 2 == 0:
            colors = ["black","white"]
        else:
            colors = ["white", "black"]
        
        t.penup()
        t.goto(ring, 55 * ring)
        t.pendown()
        for square in range(num_squares + ring * 18):
            draw_square(t, 20, colors[square % 2])
            t.forward(20)
            t.right(360 / (num_squares + ring * 18))

def main():
    """A main function creates a turtle and turtle window and calls the draw_rings function to draw the pattern"""
    kaybee = turtle.Turtle()
    kaybee.pensize(2)
    kaybee.speed("fastest")
    wn = turtle.Screen()
    wn.bgcolor("grey")
    
    draw_rings(kaybee, 18)
    turtle.exitonclick()

if __name__ == "__main__":
    main()

