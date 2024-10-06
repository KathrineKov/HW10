def find_two_smallest(numbers):
    if len(numbers) < 2:
        return "List is too short"
    numbers.sort()
    return numbers[0], numbers[1]