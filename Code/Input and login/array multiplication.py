def calculate_product(arr):
    """
    Calculates the product of all integers in the input array.

    Args:
        arr (list[int]): Input array of integers.

    Returns:
        int: Product of the values in the array.
    """
    product = 1
    for num in arr:
        product *= num
    return product

# Example usage
input_array = [2, 3, 4, 5]
result = calculate_product(input_array)
print(f"The product of the values in the input array {input_array} is {result}.")

###################
#Improve this code
from functools import reduce

def calculate_product(arr):
    """
    Calculates the product of all integers in the input array.

    Args:
        arr (list[int]): Input array of integers.

    Returns:
        int: Product of the values in the array.
    """
    if not arr:
        return 1
    return reduce(lambda x, y: x * y, arr)
