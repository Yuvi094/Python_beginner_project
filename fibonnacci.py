# Function to generate Fibonacci sequence up to n terms
def generate_fibonacci(n):
    a = 0
    b = 1
    " "
    print(f"Fibonacci sequence (first {n} numbers):")
    
    for i in range(n):
        # Print the current number in the sequence
        print(a, end=)
        
        # Update logic: 
        # 'a' becomes the next number 'b'
        # 'b' becomes the sum of 'a' and 'b'
        a, b = b, a + b

# Call the function for 8 terms
generate_fibonacci(8)