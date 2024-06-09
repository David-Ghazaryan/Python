import turtle
import random
import tkinter as tk
from tkinter import simpledialog

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor(r, g, b)

def random_position():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def draw_triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def draw_circle(radius):
    turtle.circle(radius)

def get_count(shape_name):
    root = tk.Tk()
    root.withdraw()  
    count = simpledialog.askinteger("Input", f"Մուտքագրեք {shape_name} քանակը")
    root.destroy()
    return count

def main():
    count_circle = get_count("շրջանների")
    count_triangle = get_count("եռանկյունների")
    count_square = get_count("քառակուսիների")

    screen = turtle.Screen()
    screen.colormode(255)  
    turtle.speed(0)
    turtle.pensize(2)  

    for _ in range(count_circle):
        random_color()
        random_position()
        radius = random.randint(50, 100)
        draw_circle(radius)

    for _ in range(count_triangle):
        random_color()
        random_position()
        size = random.randint(50, 100)
        draw_triangle(size)

    for _ in range(count_square):
        random_color()
        random_position()
        size = random.randint(50,100)
        draw_square(size)

    turtle.done()

if __name__ == "__main__":
    main()
