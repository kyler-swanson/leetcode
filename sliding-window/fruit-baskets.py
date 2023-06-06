def fruitIntoBaskets(fruits):
    start = 0

    substring = {}

    max_fruits = 0

    for end in range(len(fruits)):
        end_fruit = fruits[end]

        substring[end_fruit] = substring.get(end_fruit, 0) + 1

        while len(substring) > 2:
            start_fruit = fruits[start]
            substring[start_fruit] -= 1

            if substring[start_fruit] == 0:
                del substring[start_fruit]

            start += 1

        max_fruits = max(max_fruits, end - start + 1)

    return max_fruits

print(fruitIntoBaskets(['A', 'B', 'C', 'A', 'C']))
print(fruitIntoBaskets(['A', 'B', 'C', 'B', 'B', 'C']))