pet_1 = {'animal': 'cat', 'owner': 'keira'}
pet_2 = {'animal': 'dog', 'owner': 'law'}
pet_3 = {'animal': 'parrot', 'owner': 'ace'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}.")