# Given the height and width of a wall, calculate no. of cans required to paint the whole area

height_ = int(input("Enter height of the wall:  "))
width_ = int(input("Enter width of the wall:  "))

def cans_of_paint(height, width):
    no_of_cans = round((height * width) / 5)
    print(f"You need to buy {no_of_cans} cans of paint")

cans_of_paint(height_, width_)