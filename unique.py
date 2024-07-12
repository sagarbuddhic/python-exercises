# remove duplicate values

numbers = [3, 2, 3, 1, 4, 7, 4]
output = []

for item in numbers:
   if item not in output:
      output.append(item)

print(output)