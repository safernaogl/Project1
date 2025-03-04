import random
def get_random_number(n):
    """Returns a random number between 0 and n"""
    return random.randint(0, n)

def get_random_string(length):
    """Returns a random string of length 'length'"""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(letters) for i in range(length))

print(get_random_number(10)) # Output: 7
print(get_random_string(5)) # Output: kjhgf