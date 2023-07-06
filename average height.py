#  Complete the challenge without using len() and sum()

student_heights = input("Input a list of student heights. \n").split()
total_height = 0
items = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_height += student_heights[n]
    items += 1
    
average = total_height / items
print(average)