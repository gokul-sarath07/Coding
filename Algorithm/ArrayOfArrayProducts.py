# Array Of Array Products
# Example:
# Array: [2, 3, 4, 5]
# Answer: [60, 40, 30, 24]

# ==============================================================

# O(N) Time | O(N) Space

def arrayOfArrayProducts(array):
    productArray = []
    product = 1
    for i in range(len(array)):
        productArray.append(product)
        product *= array[i]
    product = 1
    for i in reversed(range(len(array))):
        productArray[i] *= product
        product *= array[i]
    return productArray

print(arrayOfArrayProducts([2, 3, 4, 5]))
