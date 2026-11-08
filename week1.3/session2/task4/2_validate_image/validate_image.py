# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except
filename = input("Enter the PGM filename: ")
with open("../images/" + filename, "r") as infile:
# Read the file content
    data = infile.readlines()

data = [line.split("#")[0].strip() for line in data]
data = [line.split() for line in data if line]
# Store the width, the height, and the maximum gray value
width = int(data[1][0])
height = int(data[1][1])
max_gray_value = int(data[2][0])

pixels = data[3:]
# For valid_pixels = True
valid_pixels = True
for row in pixels:
    for pixel in row:
        value = int(pixel)
        if value < 0 or value > max_gray_value:
            valid_pixels = False

# Check if the widths and heights are the same as specified
valid_width = True

for row in pixels:
    if len(row) != width:
        valid_width = False

valid_height = len(pixels) == height
# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value
if valid_width and valid_height and valid_pixels:
    print("Valid image")
elif not valid_width:
    print("Invalid width")
elif not valid_height:
    print("Invalid height")
elif not valid_pixels:
    print("Invalid pixel values")