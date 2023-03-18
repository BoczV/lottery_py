from user_guesses import make_guess
from lottery import pick_five_random_numbers

def main():
    print("Hey there and welcome! Lottery will start!")
    chosen_numbers = make_guess()
    print(f"You choose these numbers: {chosen_numbers}")
    lottery_numbers = pick_five_random_numbers()
    print(f"Lottery numbers: {lottery_numbers}")
    count_matches(chosen_numbers, lottery_numbers)


def count_matches(chosen_numbers, lottery_numbers):
    counter = 0
    for element in chosen_numbers:
        if(element in lottery_numbers):
            counter += 1
    print(f"You have {counter} matches.")
    if(counter > 3):
        print(f"Hurray! You won!")
    else:
        print("Better luck next time!")


if __name__=="__main__":
    main()