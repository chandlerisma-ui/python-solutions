"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    list = []
    for i in range(number, number + 3):
        list.append(i)
    return list


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    for round in rounds:
        if round == number:
            return True
    return False

def card_average(hand):
    dividor = len(hand)
    total = 0

    for card in hand:
        total += card
    return total/dividor


def approx_average_is_average(hand):
    middle_index = len(hand) // 2
    actual_average = card_average(hand)
    first_average = (hand[0] + hand[-1]) / 2
    median = hand[middle_index]

    return actual_average == first_average or actual_average == median

def average_even_is_average_odd(hand):
    even_average = card_average(hand[0::2])
    odd_average = card_average(hand[1::2])
    return even_average == odd_average
    


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
