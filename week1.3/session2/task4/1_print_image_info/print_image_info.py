# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
filename = input("Enter the PGM filename: ")
with open("../images/" + filename, "r") as infile:
    # Read the file content

    data = []
    for line in infile:
        line = line.split("#")[0]
        data.extend(line.split())

# print image dimension (i.e., Dimensions: width x height pixels)
width = data[1]
height = data[2]
print(f"Dimensions: {width} x {height} pixels")
# print max gray value (i.e., Max Gray Value: max_gray_value)
max_grey_value = data[3]
print(f"Max Gray Value: {max_grey_value}")