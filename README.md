# Final-Group-Project
Created by: Sasha, Shuwen, Kyle
Course: Creative Coding, Pratt Institute
Semester: Fall 2026

<img width="1122" height="560" alt="Example" src="https://github.com/user-attachments/assets/27e6c2ef-0f64-476f-b066-3c8f458f0a25" />


# About the Project
This project allows users to generate a poster based on three collections of a differently designed tiles. It prompts the user for canvas size and color theme, randomly creates a design, and then renders the poster along with a gallery plaque that includes the user's name and different color swatches. Most of the tiles have patterns. The program combines everyone's individual tile designs into a unified composition through a function that randomly calls corner tiles, border tiles, center tiles.

# Meet the Designers
Sasha: Playful circular designs with bright colors
Shuwen: Floral and simple designs with a soft pastel color palette 
Kyle: Brief description of their tile designs or contribution.

# Try it yourself
Copy this code into a Colab Notebook.

```python
!git clone https://github.com/kyastang/Final-Group-Project.git
%cd Final-Group-Project
!pip install -r requirements.txt
from project import generate_poster
generate_poster()
```
# How to Use
Open the notebook in Google Colab.
Run the setup cells to download the project code and install the required libraries.
Run the cell that calls the function and prompts the user to choose a title, grid dimensions, and color palette.
Your own poster will be saved as poster.svg!

# Files

- `project.py` – Main poster-generation program.
- `TileFunctions.py` – Collection of custom tile-drawing functions.
- `ColorPalettes.py` – Available color palettes.
- `requirements.txt` – Required Python libraries.
- `Example.png` – Scalable vector version of an example final poster image.

# How the code works 
We first started off by creating a 3 tile designs each for the border, corner, and center tiles. We put this information together as a collection of tile functions. We created functions for each person, with conditional geometry based on the type of tile.  Then, we each made a color palette with 4 different colors, and compiled this information as well. We defined each palette as a variable and then put them in a list.

Next, we get information for the poster. We first ask the user for a name, title, height/width, and palette, and confirm that their entries are valid. If the user selected random for the color palette, we generate the palette using random numbers.

After that, we start to generate the poster. We randomly choose which persons tile to draw and then start to draw, starting from the top left to the top right, then going from the bottom left to bottom right. While doing this, we also define the palette, correct rotation, and type of tile in the function. Next, we write the title, credits, and palette swatch colors, and rgb values at the bottom. Finally, we hide turtle, and then we're done!
