def remove_duplicates(strings):
    unique = []
    for item in strings:
        if item not in unique:
            unique.append(item)
    return unique

# Example usage
string_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
result = remove_duplicates(string_list)
print("List without duplicates:", result)
printrint("Training for EEE Class")
