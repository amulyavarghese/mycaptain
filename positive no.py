def positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return positive_numbers


list_str = input("Enter a list of numbers : ")
user_list = [int(num) for num in list_str.split()]


positive_user_list = positive_numbers(user_list)
print("Input:", user_list)
print("Output:", positive_user_list)
