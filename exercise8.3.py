def make_shirt(size, message):
    """Print a summary of the shirt's size and message."""
    print(f"The shirt is size {size} and says '{message}'.")


# positional arguments
make_shirt('large', 'I love Python')

# keyword arguments
make_shirt(size='medium', message='Hello, world')