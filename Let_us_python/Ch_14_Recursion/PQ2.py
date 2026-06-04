def fibonacci(n):
    # 1. Base Cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # 2. Recursive Case: Sum of the two preceding numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test Cases
print(fibonacci(0)) 
print(fibonacci(1))  
print(fibonacci(6))  