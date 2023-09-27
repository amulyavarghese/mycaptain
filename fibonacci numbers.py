def generate_fibonacci(limit):
    fibonacci_sequence = []
    a, b = 0, 1
    while a <= limit:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence


limit = int(input("Enter the limit for Fibonacci sequence: "))

if limit < 0:
    print("Please enter a non-negative limit.")
else:
    fibonacci_numbers = generate_fibonacci(limit)
    print("Fibonacci sequence up to", limit, "is:")
    print(fibonacci_numbers)
