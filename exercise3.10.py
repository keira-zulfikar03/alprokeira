cities = ['tokyo', 'paris', 'jakarta', 'cairo']
print(f"Original list: {cities}")

# indexing
print(f"First city: {cities[0]}")
print(f"Last city: {cities[-1]}")

# append() 
cities.append('lima')
print(f"After append: {cities}")

# insert() 
cities.insert(1, 'rome')
print(f"After insert: {cities}")

# remove() 
cities.remove('paris')
print(f"After remove: {cities}")

# pop() 
popped = cities.pop()
print(f"Popped: {popped}")
print(f"After pop: {cities}")

# del
del cities[0]
print(f"After del: {cities}")

cities.append('oslo')
cities.append('delhi')
print(f"Before sorting: {cities}")

# sorted() returns a sorted 
print(f"sorted(): {sorted(cities)}")
print(f"Original still: {cities}")

# sort() permanently
cities.sort()
print(f"After sort(): {cities}")

# reverse alphabetical order
cities.sort(reverse=True)
print(f"After sort(reverse=True): {cities}")

# reverse() flips 
cities.reverse()
print(f"After reverse(): {cities}")

# len() total
print(f"Number of cities: {len(cities)}")