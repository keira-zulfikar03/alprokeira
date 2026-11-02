favorite_languages = {
    'keira': 'python',
    'law': 'c',
    'ace': 'rust',
    'kennedy': 'python',
}

people = ['keira', 'law', 'ace', 'kennedy', 'zulfikar']

for person in people:
    if person in favorite_languages:
        print(f"Thank you for responding to the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take the poll!")