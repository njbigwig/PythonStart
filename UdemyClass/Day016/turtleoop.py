# pip install prettytable
from prettytable import PrettyTable, DOUBLE_BORDER

import turtle 
import time

my_turtle = turtle.Turtle()
print(f"{my_turtle} {type(my_turtle)}")

my_screen = turtle.Screen()
print(f"Canvas Height: {my_screen.canvheight}")

my_turtle.color('purple3')
my_turtle.shape('turtle')
my_turtle.forward(100)

#my_screen.exitonclick()

# object from a class
table = PrettyTable()

# could do in 2 lines with add_column() method
table.fieldnames = ["Pokemon Name", "Type", ]
table.add_row(["Chespin","Grass"])
table.add_row(["Qulladin","Grass"])
table.add_row(["Chesnaught","Grass-Fighting"])

print(table)

table.set_style(DOUBLE_BORDER)
print(f"Table Alignment = {table.align}")
table.align = "l"
print(table)
