# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

# print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

numbers_list = [1, 2, 3, 4, 5]

# def odd_filter(numbers_list):
#     for i in numbers_list:
#         if numbers_list[i] % 2 == 1:
#         return [numbers_list[0]]
# print(numbers_list)

# odd_filter(numbers_list)

for i in range(0, len(numbers_list)):
    odd_list = []
    if numbers_list[i] % 2 != 0 :
        odd_list.append(numbers_list[i])
    print(odd_list)