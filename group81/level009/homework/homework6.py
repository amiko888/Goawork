def remove_duplicates(arr):
  unique_elements = set(arr)
  
  return list(unique_elements)

my_array = [1, 2, 2, 3, 4, 4, 5, 1, 6]
result = remove_duplicates(my_array)

print(result) 
