def checking_number(min, max):
    """
    Returns the value which is guessed by computer
    :param min: int, minumum value of range
    :param max: int, maximum value of rnage
    :return: int, returns the counted value from range
    """
    return int((max-min)/2) + min


def guess_the_number():
    """
    Checking the given number on base of users input inforomation
    :return: str information
    """
    print('Imagine a number between 0 and 100, and I will guess it in max. 10 steps')
    min = 0
    max = 1000
    guessed = False
    while not guessed:
        guess = checking_number(min, max)
        print(f"The number is: {guess}")
        respond = input("Choose option: 'too big', 'too small', 'you guessed!'")
        if respond.lower() == 'too big':
            max = guess
        elif respond.lower() == 'too small':
            min = guess
        elif respond.lower() == 'you guessed!':
            guessed = True
            print('you win!')
        else:
            print('you gaved the wrong value')


if __name__ == "__main__":
    guess_the_number()
