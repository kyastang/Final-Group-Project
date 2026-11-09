# Final-Group-Project
Created by: Sasha, Shuwen, Kyle
Course: Creative Coding, Pratt Institute
Semester: Fall 2026

# About the Project
This project allows users to generate a poster from a three differently designed collections of tiles.  What was the idea behind your poster generator? What visual qualities or design ideas inspired it? How does the program combine everyone's individual tile designs into a unified composition?

# Meet the Designers
Sasha: Brief description of their tile designs or contribution.
Shuwen: Floral and simple designs with a soft pastel color palette 
Kyle: Brief description of their tile designs or contribution.

# Try it yourself
Copy this code into a Colab Notebook.

```
!git clone https://github.com/kyastang/Final-Group-Project
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
project.py – Main poster-generation program.
TileFunctions.py – Collection of custom tile-drawing functions.
PaletteOptions.py – Available color palettes.
requirements.txt – Required Python libraries.
example_poster.svg – Scalable vector version of an example final poster image.
