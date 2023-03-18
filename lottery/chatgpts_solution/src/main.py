import random

def generate_numbers():
    numbers = list(range(1, 91))
    random.shuffle(numbers)
    return numbers[:5]

def get_user_numbers():
    user_input = input("Kérjük, adja meg az 5 számot vesszővel elválasztva (1 és 90 között): ")
    user_numbers = user_input.split(",")
    try:
        user_numbers = [int(num.strip()) for num in user_numbers]
    except:
        print("Hibás bemenet. Kérjük, adja meg az 5 számot vesszővel elválasztva.")
        return get_user_numbers()

    if len(user_numbers) != 5 or any(num < 1 or num > 90 for num in user_numbers):
        print("Hibás bemenet. Kérjük, adja meg az 5 számot vesszővel elválasztva.")
        return get_user_numbers()

    return user_numbers

def compare_numbers():
    generated_numbers = generate_numbers()
    user_numbers = get_user_numbers()
    num_matches = len(set(generated_numbers) & set(user_numbers))
    print("Az ön találatai: ", num_matches)
    print("Az öt kisorsolt szám: ", generated_numbers)

compare_numbers()
