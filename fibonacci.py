def get_positive_integer():
    """Prompt the user for a positive integer and return it."""
    while True:
        num = input("How many terms of the Fibonacci sequence do you want? ")
        if num.isdigit() and int(num) > 0:
            return int(num)
        else:
            print("Invalid input. Please enter a positive integer.")


def generate_fibonacci(n):
    """Generate the Fibonacci sequence up to n terms and return it as a list."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_fibonacci(sequence):
    """Print the Fibonacci sequence in a readable format."""
    print("Fibonacci sequence:")
    print(" ".join(str(num) for num in sequence))


n = get_positive_integer()
fib_sequence = generate_fibonacci(n)
print_fibonacci(fib_sequence)
