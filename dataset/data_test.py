from PIL import Image, ImageDraw

# Get the input string
input_str = input("Enter the coordinates separated by commas: ").strip()

# Split the input string into pairs of coordinates
pairs = input_str.split(",")
coords = []
for i in range(0, len(pairs), 2):
    x = int(pairs[i])
    y = int(pairs[i+1])
    coords.append((x, y))

# Create a new black background image
img = Image.new("RGB", (400, 400), "black")

# Draw white circles at the specified coordinates
draw = ImageDraw.Draw(img)
for x, y in coords:
    draw.ellipse((x-1, y-1, x+2, y+2), fill="white")

# Show the resulting image
img.show()
