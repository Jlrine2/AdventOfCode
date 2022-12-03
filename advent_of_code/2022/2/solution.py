import pytest

from helpers import *
from helpers import get_full_text

INPUT = get_full_text(f"input.txt")

PART_1_SAMPLE_INPUT = get_full_text("samples/part_1_input.txt")
PART_1_SAMPLE_SOLUTION = get_full_text("samples/part_1_solution.txt")
PART_2_SAMPLE_INPUT = get_full_text("samples/part_2_input.txt")
PART_2_SAMPLE_SOLUTION = get_full_text("samples/part_2_solution.txt")


def solution_test(function, sample_input, sample_solution):
    result = function(sample_input)
    if result == sample_solution:
        return "PASS"
    return f"FAIL: got: {result} expected: {sample_solution}"



def letter_to_value(letter):
    if letter in ['A', 'X']:  # rock
        return 1
    if letter in ['B', 'Y']:  # paper
        return 2
    if letter in ['C', 'Z']:  # scissors
        return 3


def win_or_lose(elf, me):
    loop = [1, 2, 3]
    if loop[letter_to_value(me) - 2] == letter_to_value(elf):
        return 6
    if letter_to_value(elf) == letter_to_value(me):
        return 3
    return 0


def part_1_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input)

    points = 0
    for line in lines:
        elf = line.split(' ')[0]
        me = line.split(' ')[1]
        points += letter_to_value(me)
        points += win_or_lose(elf, me)

    return str(points)


def part_2_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input)

    points = 0
    for line in lines:
        elf = line.split(' ')[0]
        me = line.split(' ')[1]
        if me == "Y":
            points += 3 + letter_to_value(elf)
        if me == "X":
            for x in 'ABC':
                if win_or_lose(elf, x) == 0:
                    points += letter_to_value(x)
        if me == "Z":
            for x in 'ABC':
                if win_or_lose(elf, x) == 6:
                    points += 6 + letter_to_value(x)
    return str(points)


if __name__ == "__main__":
    if not INPUT:
        INPUT = download_input(*year_and_date(__file__))
        with open("input.txt", "wb") as f:
            f.write(INPUT)
    part_1 = solution_test(part_1_solution, PART_1_SAMPLE_INPUT, PART_1_SAMPLE_SOLUTION)
    part_2 = solution_test(part_2_solution, PART_2_SAMPLE_INPUT, PART_2_SAMPLE_SOLUTION)

    print(f"Part_1: {part_1}")
    print(f"Part_2: {part_2}")
    print('---SOLUTIONS---')
    print(f"Part_1: {part_1_solution(INPUT)}")
    print(f"Part_2: {part_2_solution(INPUT)}")
