# Incorporating in Calculations
numbers = [10, 20, 30]
sum = numbers[0] + numbers[1]  # Adds 10 and 20


numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)


original_list = [[1, 2, 3], [4, 5, 6]]
copied_list = original_list.copy()
copied_list[0][0] = 100

print(original_list)
print(copied_list)


words = ["Hello", "world", "Python"]
sentence = " ".join(words)
print(sentence)

numbers = [1, 2, 3]
result = "-".join(map(str, numbers))
print(result)