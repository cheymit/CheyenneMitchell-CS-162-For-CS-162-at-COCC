# Function to compute the area of a rectangle
def rect_area(length, width):
    return length * width

# Function to compute the surface area of a rectangular solid
def rect_surface_area(length, width, height):
    # Reuse rect_area for all face pairs
    side1 = rect_area(length, width)     # Top/Bottom
    side2 = rect_area(length, height)    # Front/Back
    side3 = rect_area(width, height)     # Left/Right

    return 2 * (side1 + side2 + side3)   # this will show us the Total surface area = 2 of each face

# --- Main Program ---

# User input
length = int(input("Enter the length of the rectangular solid: "))
width = int(input("Enter the width of the rectangular solid: "))
height = int(input("Enter the height of the rectangular solid: "))

# This calculates the surface area
surface_area = rect_surface_area(length, width, height)

# Output results
print() #blank
print("Dimensions:")
print("Length =", length)
print("Width =", width)
print("Height =", height)
print("Surface Area of Rectangular Solid =", surface_area)