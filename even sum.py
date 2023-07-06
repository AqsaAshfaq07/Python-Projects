even_sum = 0
for num in range(2, 101, 2):
    even_sum += num
    
print(even_sum)

# OR

total = 0
for num in range(2, 101):
    if num %2 == 0:
        total += num
        
print(total)