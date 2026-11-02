def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    'law', 'smith',
    location='solo',
    field='industrial engineering',
    hobby='gaming',
)
print(my_profile)