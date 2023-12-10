
# Q.61 Write a Python program to returns sum of all divisors of a number 

# import math

# def sum_of_divisors(number):
#     # Initialize the sum
#     divisor_sum = 0

#     # Iterate up to the square root of the number
#     for i in range(1, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             # If 'i' is a divisor, add it to the sum
#             divisor_sum += i

#             # If the divisor is not the square root of the number, add its pair
#             if i != number // i:
#                 divisor_sum += number // i

#     return divisor_sum

# # Taking user input for the number
# num = int(input("Enter a number: "))

# result = sum_of_divisors(num)
# print(f"The sum of all divisors of {num} is: {result}")

###########
# def get_divisors(number):
#     divisors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             divisors.append(i)
#     return divisors

# # Taking user input for the number
# num = int(input("Enter a number: "))

# result = get_divisors(num)
# print(f"The divisors of {num} are: {result}")

###################################################################################################################3

# Q.62 Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

# def find_max_min(numbers):
#     if not numbers:
#         return None, None  # If the list is empty, return None for both max and min

#     max_num = numbers[0]  # Assume the first number is the maximum
#     min_num = numbers[0]  # Assume the first number is the minimum

#     for num in numbers:
#         if num > max_num:
#             max_num = num  # Update max_num if a larger number is found
#         elif num < min_num:
#             min_num = num  # Update min_num if a smaller number is found

#     return max_num, min_num

# # Example usage:
# decimal_numbers = [3.14, 2.71, 5.5, 1.618, 0.707]
# maximum, minimum = find_max_min(decimal_numbers)
# print(f"The maximum number is: {maximum}")
# print(f"The minimum number is: {minimum}")

