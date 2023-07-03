row1 = [' . ',' . ',' . ']
row2 = [' . ',' . ',' . ']
row3 = [' . ',' . ',' . ']

map = [row1, row2, row3]  # a map of blank squares  3-by-3
# print(f"{row1}\n{row2}\n{row3}")

location = input("Where do you want to put the treasure? \nEnter the row and column number")
loc_list = location.split(" ")

x = int(loc_list[0]) - 1
y = int(loc_list[1]) - 1

map[x][y] = 'X'
print(map)