import random
import sys


def makeMessage(value):
    return f"You rolled {value}."


def roll_dice():
    return random.randint(1, 6)


def roll_dice_multiple_times(times=0):
    values = []

    if times == 0:
        values.append(roll_dice())
        return values

    for _ in range(times):
        values.append(roll_dice())

    return values


if __name__ == "__main__":
    args = sys.argv

    if (len(args) > 1):
        try:
            times = int(args[1])
            values = roll_dice_multiple_times(times)

            for value in values:
                print(makeMessage(value))

        except ValueError:
            print(f'{args[1]} is not a number')
    else:
        values = roll_dice_multiple_times()

        for value in values:
            print(makeMessage(value))
