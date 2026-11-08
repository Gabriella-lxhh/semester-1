# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except
filename = input("Enter the PGM filename: ")

with open("../images/" + filename, "r") as infile:
    data = infile.readlines()

data = [line.split("#")[0].strip() for line in data]
data = [line.split() for line in data if line]

width = int(data[1][0])
height = int(data[1][1])
max_gray = int(data[2][0])
pixels = data[3:]
# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value
inverted_pixels = []

for row in pixels:
    inverted_row = [max_gray - int(pixel) for pixel in row]
    inverted_pixels.append(inverted_row)

# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"
with open("inverted_" + filename, "w") as outfile:
    outfile.write("P2\n")
    outfile.write(f"{width} {height}\n")
    outfile.write(f"{max_gray}\n")
    for row in inverted_pixels:
        string_row = " ".join(str(pixel) for pixel in row)
        outfile.write(string_row + "\n")