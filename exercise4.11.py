pizzas = ['pepperoni', 'margarita', 'hawaiian']
friend_pizzas = pizzas[:]   # slice copy

pizzas.append('four cheese')
friend_pizzas.append('bbq chicken')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)