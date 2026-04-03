
def generate_fibonacci(n):
    a = 0
    b = 1
    " "
    print(f"Fibonacci sequence (first {n} numbers):")
    for i in range(n):
        print(a)
        a, b = b, a + b
generate_fibonacci(8)
