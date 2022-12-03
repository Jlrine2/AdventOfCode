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


def part_1_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input)

    # Solution code goes here
    return ''


def part_2_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input)

    # Solution code goes here
    return ''


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
