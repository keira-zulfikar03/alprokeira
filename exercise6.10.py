favorite_numbers = {
    'keira': [7, 14],
    'law': [3],
    'ace': [21, 5, 9],
    'kennedy': [10, 1],
    'zulfikar': [8, 88],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")