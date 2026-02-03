def is_divisible(n, *numbers):
    index = 0
    for i in numbers:
        if numbers[index] % i == 0:
            return True
        index += 1
    return False
print(is_divisible(3,3,4))