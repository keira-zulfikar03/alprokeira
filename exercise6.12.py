cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10_500_000,
        'fact': 'It is the capital of Indonesia.',
        'visited': True,
    },
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'fact': 'It hosted the Olympics in 1964 and 2021.',
        'visited': False,
    },
    'paris': {
        'country': 'france',
        'population': 2_100_000,
        'fact': 'The Eiffel Tower was finished in 1889.',
        'visited': False,
    },
}

for city, info in cities.items():
    status = "visited" if info['visited'] else "not visited yet"
    print(f"{city.title()}, {info['country'].title()} ({status})")
    print(f"  Population: {info['population']:,}")
    print(f"  Fact: {info['fact']}\n")