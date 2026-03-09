def count(arr, number):
    count = 0
    for i in arr:
        if i == number:
            count += 1
    return count

numbers = [1, 2, 3, 2, 4, 2, 5]
result = count(numbers, 2)
print(result)  

