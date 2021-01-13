# Nth Fibonacci
# Example:
# Number: 10
# Answer: 34

# ==============================================================

# O(N) Time | O(1) Space

def nthFibonacci(n):
    twoValues = [0, 1]
    counter = 3
    while counter <= n:
        nextValue = twoValues[0] + twoValues[1]
        twoValues[0] = twoValues[1]
        twoValues[1] = nextValue
        counter += 1
    return twoValues[1] if n > 1 else twoValues[0]

print(nthFibonacci(10))
