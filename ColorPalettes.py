palette_options = {}

random = {
    "bg": (np.random.randint(256), np.random.randint(256), np.random.randint(256)),
    "primary": (np.random.randint(256), np.random.randint(256), np.random.randint(256)),
    "secondary": (np.random.randint(256), np.random.randint(256), np.random.randint(256)),
    "accent": (np.random.randint(256), np.random.randint(256), np.random.randint(256)),
}

# Color palette for person 1 here
sasha_palette = {
        "bg": (167, 196, 194),
        "primary": (255, 165, 165),
        "secondary": (236, 54, 141),
        "accent": (46, 2, 25)
    }
# Add this line at the end
palette_options["sasha"] = sasha_palette

# Color palette for person 2 here
shuwen_palette = {
        "bg": (250, 245, 220),
        "primary": (250, 210, 230),
        "secondary": (135, 230, 215),
        "accent": (65, 65, 120)
    }
# Add this line at the end
palette_options["shuwen"] = shuwen_palette

# Color palette for person 3 here
kyle_palette = {
        "bg": (64, 4, 4),
        "primary": (80, 115, 255),
        "secondary": (240, 140, 40),
        "accent": (200, 10, 20)
    }
# Add this line at the end
palette_options["kyle"] = kyle_palette

# Run this cell to look at all the names.

palette_names = list(palette_options)
palette_names.append("random")
print(f"The available color palettes are: {palette_names}")
