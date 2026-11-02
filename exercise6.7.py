person_1 = {
    'first_name': 'law',
    'last_name': 'smith',
    'age': 20,
    'city': 'solo',
}
person_2 = {
    'first_name': 'keira',
    'last_name': 'z',
    'age': 19,
    'city': 'jakarta',
}
person_3 = {
    'first_name': 'ace',
    'last_name': 'portgas',
    'age': 21,
    'city': 'bandung',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"{full_name}, age {person['age']}, lives in {person['city'].title()}.")