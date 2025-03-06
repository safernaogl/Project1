import random
def get_random_code():
    code = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(8))
    return code