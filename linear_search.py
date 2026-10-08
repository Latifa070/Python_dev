def linear_search(list, target):
    """
    return the index position of a value or return none if not found
    """
    for value in range(0,len(list)):
        if list[value] == target:
            return value
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("The target not found")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers,15)

verify(result)
