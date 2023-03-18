def get_valid_input():
    chosen_numbers = []
    while len(chosen_numbers) != 5:
        user_input = input("Pick 5 numbers from 0 to 90, separated by commas: ")
        chosen_numbers = validate_input(user_input)
    return chosen_numbers


def validate_input(user_input):
    str_list = user_input.split(", ")
    if(len(str_list) != 5):
        str_list = user_input.split(",")
        if(len(str_list) != 5):
            print("Wrong input!")
            return []
    return process_input(str_list)


def process_input(str_list):
    int_set = set([])
    for element in str_list:
        try:
            int_element = int(element)
            if(int_element < 0 or int_element > 90):
                print("Wrong input!")
                return []
        except:
            print("Wrong input!")
            return []
        int_set.add(int_element)
    if(len(int_set) != 5):
        print("Wrong input!")
    return list(int_set)


def make_guess():
    chosen_numbers = get_valid_input()
    return chosen_numbers

