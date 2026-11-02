def describe_city(city, country='indonesia'):
    """Print which country a city is in."""
    print(f"{city.title()} is in {country.title()}.")


describe_city('jakarta')
describe_city('solo')
describe_city('tokyo', 'japan')