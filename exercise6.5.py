danau = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in danau.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe rivers in the dictionary are:")
for river in danau.keys():
    print(river.title())

print("\nThe countries in the dictionary are:")
for country in danau.values():
    print(country.title())