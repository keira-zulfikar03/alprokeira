my_food = [ "apple", "coffee", "matcha", ]
friends_food = my_food[:]

my_food.append("chocolate")
friends_food.append("ice cream")

print("My favorite foods are:")
for food in my_food:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friends_food:
    print(food)