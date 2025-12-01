import statistics
# Ask user to input any ten numbers
user_numbers = []
# Uses a for loop to get 10 numbers from the user
for i in range(10):
    number = float(
        input(f"Please enter any number, with or without a decimal {i + 1}: "))
    user_numbers.append(number)
# Calculates the sum, maximum, minimum, mean, and median of the numbers
total = sum(user_numbers)
print(f"The sum of the numbers you entered is: {total}")
max_index = user_numbers.index(max(user_numbers))
print(f"The largest number you entered is: {user_numbers[max_index]}")
min_index = user_numbers.index(min(user_numbers))
print(f"The smallest number you entered is: {user_numbers[min_index]}")
mean_value = statistics.mean(user_numbers)
print(f"The mean of the numbers you entered is: {mean_value}")
median_value = statistics.median(user_numbers)
print(f"The median of the numbers you entered is: {median_value}")
