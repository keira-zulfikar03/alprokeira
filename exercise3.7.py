names = ['keira', 'law', 'ace', 'kennedy']
print(f"hello, {names[0]}, you are invited to my birthday party!")
print(f"hello, {names[1]}, you are invited to my birthday party!")
print(f"hello, {names[2]}, you are invited to my birthday party!")
print(f"hello, {names[3]}, you are invited to my birthday party!")

print(f"{names[0]}, cant make it")

names = ['zulfikar', 'law', 'ace', 'kennedy']
print(f"hello, {names[0]}, you are invited to my birthday party!")
print(f"hello, {names[1]}, you are invited to my birthday party!")
print(f"hello, {names[2]}, you are invited to my birthday party!")
print(f"hello, {names[3]}, you are invited to my birthday party!")

print("found bigger table!")

names.insert(0, 'joshua')   #add to beginning
names.insert(2, 'markisa') #add to middle
names.append('sarah') #add to end
print(f"hello, {names[0]}, you are invited to my birthday party!")
print(f"hello, {names[1]}, you are invited to my birthday party!")
print(f"hello, {names[2]}, you are invited to my birthday party!")
print(f"hello, {names[3]}, you are invited to my birthday party!")
print(f"hello, {names[4]}, you are invited to my birthday party!")
print(f"hello, {names[5]}, you are invited to my birthday party!")

print("Sorry, the new table won't arrive in time. I can only invite two people for dinner.")

removed = names.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")

removed = names.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")

removed = names.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")

removed = names.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")

removed = names.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")

print(f"{names[0]}, you are still invited to dinner!")
print(f"{names[1]}, you are still invited to dinner!")

del names[1]
del names[0]

print(names)