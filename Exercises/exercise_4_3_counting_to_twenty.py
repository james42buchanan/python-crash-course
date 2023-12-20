# numbers = list()
# for number in range(1_000_001):
#     numbers.append(number)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

cubes = [number**3 for number in range(1, 11)]
print(cubes)

cubes_2 = list()
for number in range(1, 11):
    cubes_2.append(number**3)
print(cubes_2)