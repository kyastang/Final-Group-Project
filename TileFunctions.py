# Function definition for person 1 here
# Insert your name in the function name.
# Do not change anything else yet!
def draw_sasha_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

      big_r = quarter * 0.8
      small_r = quarter * 0.4
      c = half - big_r - 5   # distance from center to the big circle's center

      # Big circle
      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(c)
      t.left(90)
      t.forward(c)
      t.right(90)
      t.right(90)
      t.forward(big_r)      # step back so the circle's center lands here
      t.left(90)
      t.color(palette["accent"], palette["primary"])
      t.pensize(2)
      t.pendown()
      t.begin_fill()
      t.circle(big_r)
      t.end_fill()
      t.penup()

      # Small circle along one edge
      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(c - big_r - small_r - 5)
      t.left(90)
      t.forward(c)
      t.right(90)
      t.right(90)
      t.forward(small_r)
      t.left(90)
      t.color(palette["accent"], palette["secondary"])
      t.pendown()
      t.begin_fill()
      t.circle(small_r)
      t.end_fill()
      t.penup()

      # Small circle along the other edge
      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(c)
      t.left(90)
      t.forward(c - big_r - small_r - 5)
      t.right(90)
      t.right(90)
      t.forward(small_r)
      t.left(90)
      t.color(palette["accent"], palette["secondary"])
      t.pendown()
      t.begin_fill()
      t.circle(small_r)
      t.end_fill()
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

      circle_radius = size * 0.14
      spacing = size / 3.0

      for i in range(-1, 2):
          t.penup()
          t.jumpto(x, y)
          t.setheading(rotation)

          t.forward(i * spacing)
          t.right(90)
          t.forward(half - circle_radius * 0.2)
          t.left(90)

          t.color(palette['accent'], palette['secondary'])
          t.pensize(2)
          t.pendown()
          t.begin_fill()
          t.circle(circle_radius)
          t.end_fill()
          t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)




  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  elif tile_type == "center":

      big_r = quarter * 0.6
      dot_r = quarter * 0.3
      petal = quarter * 1.4

      t.color(palette["secondary"], palette["secondary"])
      t.pensize(2)
      for i in range(8):
          t.penup()
          t.jumpto(x, y)
          t.setheading(rotation + i * 45 - 30)
          t.pendown()
          t.begin_fill()
          for j in range(3):
              t.forward(petal)
              t.left(120)
          t.end_fill()
          t.penup()


      t.color(palette["accent"], palette["primary"])
      for i in range(8):
          t.jumpto(x, y)
          t.setheading(rotation + i * 45)
          t.forward(quarter * 1.5)
          t.right(90)
          t.forward(dot_r)
          t.left(90)
          t.pendown()
          t.begin_fill()
          t.circle(dot_r)
          t.end_fill()
          t.penup()


      t.jumpto(x, y)
      t.setheading(rotation)
      t.right(90)
      t.forward(big_r)
      t.left(90)
      t.color(palette["accent"], palette["primary"])
      t.pendown()
      t.begin_fill()
      t.circle(big_r)
      t.end_fill()
      t.penup()


      t.jumpto(x, y)
      t.dot(quarter * 0.4, palette["accent"])




  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

  # Function definition for person 2 here
def draw_shuwen_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(quarter)
      t.right(60)
      t.forward(quarter)
      t.left(180)

      t.pendown()
      t.forward(half)
      t.left(90)
      t.forward(half)
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.color(palette["secondary"], palette["primary"])
      t.forward(quarter + quarter / 2)
      t.left(90)
      t.forward(quarter)

      t.pendown()
      t.begin_fill()
      t.circle(quarter / 2)
      t.end_fill()
      t.left(90)
      t.forward(quarter / 2)
      t.color(palette["secondary"])
      t.dot(quarter / 4)
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.color(palette["accent"], palette["primary"])
      t.forward(-half)
      t.left(90)
      t.forward(-half)
      t.right(90)

      t.pendown()
      t.begin_fill()
      for _ in range(2):
          t.forward(size)
          t.left(90)
          t.forward(quarter)
          t.left(90)
      t.end_fill()
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["secondary"])
      t.pensize(2)
      t.forward(-half)
      t.pendown()
      t.forward(size)
      t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      t.color(palette["secondary"], palette["primary"])
      t.setheading(rotation + 60)
      for i in range(4):
        t.jumpto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(3):
            t.circle(quarter)
        t.end_fill()
        t.penup()
        t.left(90)

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(6)

      for _ in range(4):
          t.pendown()
          t.circle(4)
          t.penup()
          t.jumpto(x, y)
          t.right(90)

      t.pencolor(palette["accent"])
      t.pensize(2)
      t.jumpto(x, y)
      t.setheading(rotation + 45)
      t.forward(quarter * 1.2)
      t.left(90)
      t.forward(quarter * 1.2)
      t.pendown()
      for i in range(4):
          t.left(90)
          t.forward(half * 1.2)
      t.left(45)
      t.penup()

      t.forward(half * 0.9)


  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

  # Function definition for person 3 here
def draw_kyle_tile(t, x, y, size, rotation, palette, tile_type="center"):

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # HELPER: go_to(dx, dy)
  # Moves the turtle (with the pen UP) to a spot measured from the
  # CENTER of the tile. dx = steps to the right, dy = steps up.
  # Because it uses the tile's rotation, my shapes turn with the tile!
  # Example: go_to(0, 0) is the center, go_to(-half, -half) is the
  # bottom-left corner. The turtle ends up facing along the rotation.
  # ==========================================
  def go_to(dx, dy):
      t.penup()
      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(dx)
      t.left(90)
      t.forward(dy)
      t.right(90)

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # A big square tucked into the corner with an "L" frame around it
  # ------------------------------------------
  if tile_type == "corner":


      go_to(-half, -half)
      t.color(palette["primary"], palette["primary"])
      t.pendown()
      t.begin_fill()
      for _ in range(4):
          t.forward(half)
          t.left(90)
      t.end_fill()
      t.penup()


      go_to(-quarter, -quarter)
      t.color(palette["secondary"])
      t.dot(quarter)


      go_to(-half, quarter)
      t.color(palette["accent"])
      t.pensize(3)
      t.pendown()
      t.forward(size * 0.75)    # go right
      t.right(90)
      t.forward(size * 0.75)    # go down
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":


      go_to(-half, -half)
      t.color(palette["primary"], palette["primary"])
      t.pendown()
      t.begin_fill()
      for _ in range(2):
          t.forward(size)
          t.left(90)
          t.forward(quarter)
          t.left(90)
      t.end_fill()
      t.penup()


      for i in range(4):
          go_to(-half + size * (i + 0.5) / 4, -half + quarter / 2)
          t.color(palette["secondary"])
          t.dot(quarter / 2)


      go_to(-half, -half + quarter)
      t.color(palette["accent"])
      t.pensize(3)
      t.pendown()
      t.forward(size)
      t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:


      go_to(0, -half * 0.8)
      t.setheading(rotation + 45)
      t.color(palette["primary"], palette["primary"])
      t.pendown()
      t.begin_fill()
      for _ in range(4):
          t.forward(half * 1.13)    # side length of the diamond
          t.left(90)
      t.end_fill()
      t.penup()


      go_to(0, 0)
      t.color(palette["accent"])
      t.pensize(2)
      for _ in range(8):
          t.pendown()
          t.forward(half * 0.95)
          t.backward(half * 0.95)
          t.penup()
          t.left(45)


      go_to(0, -quarter)
      t.color(palette["secondary"], palette["secondary"])
      t.pendown()
      t.begin_fill()
      t.circle(quarter)
      t.end_fill()
      t.penup()


      go_to(0, 0)
      t.color(palette["accent"])
      t.dot(quarter / 2)


      for dx, dy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
          go_to(dx * half * 0.8, dy * half * 0.8)
          t.color(palette["primary"])
          t.dot(quarter / 2)

  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  t.pencolor(palette["secondary"])
  t.pensize(2)


  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)


  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

tile_functions = [draw_sasha_tile, draw_shuwen_tile, draw_kyle_tile]
