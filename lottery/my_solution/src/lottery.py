import random

def pick_one_random_number(result):
    random_num = random.randint(1, 90) 
    while random_num in result:
        random_num = random.randint(1, 90)
    return random_num


def pick_five_random_numbers():
    result = []
    for i in range(0, 5):
        result.append(pick_one_random_number(result))
    return result