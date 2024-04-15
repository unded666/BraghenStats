import numpy as np
import matplotlib.pyplot as plt

def roll_x_by_n_dice(x, n) -> list:
    """
    rolls n sets of x dice, returned as tuples

    :param x: number of dice in each experiment n
    :param n: number of experiments
    :return: dice rolls
    """

    rolls = [tuple(np.random.randint(1, 7, x)) for i in range(n)]

    return rolls

def Braghenise(list_of_rolls) -> list:
    """
    Braghenise a list of dice rolls. This is done by replacing all die rolls of '1' with '6'

    :param list_of_rolls: list of dice rolls
    :return: braghenised list
    """

    braghenised = [tuple([6 if die == 1 else die for die in roll]) for roll in list_of_rolls]

    return braghenised

def sum_dice_rolls(list_of_rolls) -> list:
    """
    sums the dice rolls in a list

    :param list_of_rolls: list of dice rolls
    :return: list of sums
    """

    sums = [sum(roll) for roll in list_of_rolls]

    return sums

if __name__ == '__main__':
    # debugging code here

    # roll 2 dice 10 times
    rolls = roll_x_by_n_dice(2, 10)
    print(rolls)