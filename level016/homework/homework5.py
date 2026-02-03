def in_array(array1, array2):
    result = []
    for i in array1:
        for j in array2:
            if i in j:
                result.append(i)
                break
    return sorted(result)