def remove_duplicates(sequence):
    seen = set()
    return [item for item in sequence if not (item in seen or seen.add(item))]


input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result) 
