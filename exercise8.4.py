def make_shirt(size='large', message='I love Python'):
    """Print a summary of the shirt's size and message."""
    print(f"The shirt is size {size} and says '{message}'.")


# default
make_shirt()

# medium default
make_shirt(size='medium')

# any size, different message
make_shirt('small', 'Hello, world')

def make_shirt(size='large', message='I love Python'):
    """Print a summary of the shirt's size and message."""
    print(f"The shirt is size {size} and says '{message}'.")