import random

def generate_random_code():
    code = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(10))
    return code
