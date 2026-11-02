glossary = {
    'variable': 'A name that stores a value.',
    'list': 'An ordered collection of items that can be changed.',
    'tuple': 'An ordered collection of items that cannot be changed.',
    'loop': 'Code that repeats a block of instructions.',
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A series of characters, such as text.',
    'comment': 'A note in the code, starting with #, that Python ignores.',
    'index': 'The position of an item in a list, starting from 0.',
    'method': 'A function that belongs to an object, like append().',
    'slice': 'A part of a list, such as the first three items.',
}

for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"\t{meaning}\n")