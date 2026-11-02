favorite_places = {
    'keira': ['bali', 'new york'],
    'law': ['tokyo'],
    'ace': ['bandung', 'netherlands', 'malang'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")