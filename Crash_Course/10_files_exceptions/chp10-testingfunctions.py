# Testing A Function

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

print(get_formatted_name('tomas', 'quinones'))