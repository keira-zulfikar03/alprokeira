prompt = "\nEnter a pizza topping (or 'quit' to finish): "
topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
        
prompt = "\nEnter a pizza topping (or 'quit' to finish): "
active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")
        