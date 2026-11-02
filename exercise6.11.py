cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10_500_000,
        'fact': 'It is the capital of Indonesia.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'fact': 'It hosted the Olympics in 1964 and 2021.',
    },
    'paris': {
        'country': 'france',
        'population': 2_100_000,
        'fact': 'The Eiffel Tower was finished in 1889.',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']:,}")
    print(f"\tFact: {info['fact']}")