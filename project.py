from ColabTurtlePlus.Turtle import *
import numpy as np

from TileFunctions import *
from ColorPalettes import *


def generate_poster():

  name_text = input("Enter your name: ")
  title_text = input("Enter a title for your poster: ")
  
  nrows = int(input("Grid height: "))
  while nrows < 3 or nrows > 8:
    print("Should be between 3 and 8.")
    nrows = int(input("Grid height: "))
  
  ncols = int(input("Grid width: "))
  while ncols < 3 or ncols > 8:
    print("Should be between 3 and 8.")
    ncols = int(input("Grid width: "))
  
  p_name = input("Enter the name of the color palette you wish to use: ").lower()
  while p_name not in palette_names:
    print(f"Invalid palette name. The valid names are {palette_names}.")
    p_name = input("Enter the name of the color palette you wish to use: ").lower()
  
  print(f"You have selected the {p_name} palette.")
  
  if p_name == "random":
    print("Now generating a random color palette...")
    palette = random
  else:
    palette = palette_options[p_name]
  
  print("Success! Now generating your poster...")
  
  clearscreen()
  setup(1000, 500)
  t = Turtle()
  t.speed(0)
  
  y_offset = 200
  x_offset = -450
  size = 50
  
  #Variables for grid & quadrants
  row_half = nrows//2
  col_half = ncols//2
  row_max = nrows-1
  col_max = ncols-1
  
  #Grid
  for row in range(nrows):
    y = y_offset - size * row
  
    for col in range(ncols):
      x = x_offset + size * col
  
      # Randomly choose which person's tile to draw
      F = tile_functions[np.random.randint(len(tile_functions))]
  
      # Top left
      if(row < row_half) and (col < col_half):
        rotation = 90
        # Top left most position
        if(row == 0) and (col == 0):
          F(t, x, y, size, rotation, palette, "corner")
        # First row position
        elif(row == 0):
          F(t, x, y, size, rotation - 270, palette, "border")
        elif(col == 0):
          F(t, x, y, size, rotation - 180, palette, "border")
        else:
          F(t, x, y, size, rotation-90, palette, "center")
  
      # Top right
      elif (row < row_half) and (col_half < col_max):
        rotation = 0
        if(col == col_max) and (row == 0):
          F(t, x, y, size, rotation, palette, "corner")
        elif(row == 0):
          F(t, x, y, size, rotation - 180, palette, "border")
        elif(col == col_max):
          F(t, x, y, size, rotation - 270, palette, "border")
        else:
          F(t, x, y, size, rotation - 90, palette, "center")
  
      # Bottom left
      elif(row_half < row_max) and (col < col_half):
        rotation = 180
        if(col == 0) and (row == row_max):
          F(t, x, y, size, rotation, palette, "corner")
        elif(col == 0):
          F(t, x, y, size, rotation - 270, palette, "border")
        elif(row == row_max):
          F(t, x, y, size, rotation - 180, palette, "border")
        else:
          F(t, x, y, size, rotation - 90, palette, "center")
  
      # Bottom right
      elif(row_half < row_max) and (col_half < col_max):
        rotation = 270
        if(col == col_max) and (row == row_max):
          F(t, x, y, size, rotation, palette, "corner")
        elif(col == col_max):
          F(t, x, y, size, rotation - 180, palette, "border")
        elif(row == row_max):
          F(t, x, y, size, rotation - 270, palette, "border")
        else:
          F(t, x, y, size, rotation - 90, palette, "center")
  
  # Write the title and credits
  t.jumpto(0, 0)
  t.pencolor(palette["primary"])
  t.write(title_text, align="center", font=(25, "Georgia", "bold"))
  t.setheading(270)
  t.forward(30)
  t.pencolor(palette["primary"])
  t.write(name_text, align="center", font=(15, "Georgia", "italic"))
  
  # Draw the color palette colors
  t.jumpto(x_offset, -200)
  for v in palette.values():
    t.color(v, v)
    t.setheading(90)
    t.pendown()
  
    # Draw rectangle.
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.end_fill()
  
    t.penup()
    t.right(180)
    t.forward(50)
    t.right(90)
    t.forward(20)
    # Write the RGB values
    t.write(v, align="center")
    t.setheading(0)
    t.forward(80)
    t.left(90)
    t.forward(20)
  
  t.hideturtle()
  t.done()
saveSVG("/content/poster.svg")
