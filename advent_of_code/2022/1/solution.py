import pytest

from helpers import *
from helpers import get_full_text

INPUT = get_full_text(f"input.txt")

PART_1_SAMPLE_INPUT = get_full_text("samples/part_1_input.txt")
PART_1_SAMPLE_SOLUTION = get_full_text("samples/part_1_solution.txt")
PART_2_SAMPLE_INPUT = get_full_text("samples/part_2_input.txt")
PART_2_SAMPLE_SOLUTION = get_full_text("samples/part_2_solution.txt")


def part_1_solution_test():
    if part_1_solution(PART_1_SAMPLE_INPUT) == PART_1_SAMPLE_SOLUTION:
        return "PASS"
    return "FAIL"


def part_2_solution_test():
    if part_2_solution(PART_2_SAMPLE_INPUT) == PART_2_SAMPLE_SOLUTION:
        return "PASS"
    return "FAIL"


def part_1_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input,)
    lines.append('')
    elf_food = []
    max_calories = 0
    for line in lines:
        if line == '':
            calories = sum(elf_food)
            if calories > max_calories:
                max_calories = calories
            elf_food = []
        else:
            elf_food.append(int(line))
    return str(max_calories)


def part_2_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input)
    lines.append('')
    elf_food = []
    elf_calories = []
    for line in lines:
        if line == '':
            calories = sum(elf_food)
            elf_calories.append(calories)
            elf_food = []
        else:
            elf_food.append(int(line))
    return str(sum(sorted(elf_calories)[:-4:-1]))


if __name__ == "__main__":
    if not INPUT:
        print("Downloading Input")
        INPUT = download_input(*year_and_date(__file__))
        with open("input.txt", "wb") as f:
            f.write(INPUT.encode())

    part_1_status = part_1_solution_test()
    part_1_solution_output = part_1_solution(INPUT)
    print(f"Part_1: {part_1_status} -- Full Solution: {part_1_solution_output}")

    print(f"Part_2: {part_2_solution_test()} -- Full Solution: {part_2_solution(INPUT)}")
