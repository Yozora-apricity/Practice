count = 0
for _ in range(10):
    if int(input("Enter a number: ")) % 2:
        count += 1
        
print("There are", (count), "odd numbers.")