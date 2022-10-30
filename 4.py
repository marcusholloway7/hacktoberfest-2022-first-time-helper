# Import Tkinter
from tkinter import *
# globally declare the expression variable
expression = ""
# Function to update expression in the text entry box
def press(num):
 global expression
 expression = expression + str(num)
 equation.set(expression)
# Function to evaluate the final expression
def equalpress():
 try:
  global expression
  total = str(eval(expression))
equation.set(total)
  expression = ""
except:
equation.set(" error ")
  expression = ""