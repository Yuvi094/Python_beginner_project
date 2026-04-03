# function to generate a fibonacci sequence up to n terms
def generate_fibonacci(n):
    a = 0
    b = 1

    print(f"Fibonacci sequence (first {n} numbers):")
    
    for i in range(n):
       # Show the first no.
       print (a)
       # Print the next no.
       c = a + b
       # shift a to next number to be added in the next loop
       a = b
       # shift a to c so that new b is added in next loop
       b = c

# Call the function for 8 terms
generate_fibonacci(8)
