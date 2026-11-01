foods = ('rice', 'fried chicken', 'noodles', 'salad', 'soup')

print("The menu is:")
for food in foods:
    print(food)

# foods[0] = 'bread'   # TypeError

# menu changes: rewrite the whole tuple
foods = ('rice', 'pizza', 'noodles', 'salad', 'pasta')

print("\nThe revised menu is:")
for food in foods:
    print(food)