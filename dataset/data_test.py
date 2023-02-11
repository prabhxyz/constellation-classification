from PIL import Image, ImageDraw
def plot_circles(coords):
    # Create a black image of size 400x400
    img = Image.new("RGB", (400, 400), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Draw white circles at each coordinate with a radius of 3
    for coord in coords:
        draw.ellipse((coord[0] - 3, coord[1] - 3, coord[0] + 3, coord[1] + 3), fill=(255, 255, 255),
                     outline=(255, 255, 255))
    # Show the image
    img.show()

# Unpack
def convert_to_tuples(coords):
    tuples = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]
    return tuples

# Test Data (This is example data)
coords = [372,395,239,445,269,264,225,192,218,36,-21,113]
coords = convert_to_tuples(coords)

# Test Coordinates
plot_circles(coords)
