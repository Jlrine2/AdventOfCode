import pytest

from helpers import *
from helpers import get_full_text

INPUT = get_full_text(f"input.txt")

PART_1_SAMPLE_INPUT = get_full_text("samples/part_1_input.txt")
PART_1_SAMPLE_SOLUTION = get_full_text("samples/part_1_solution.txt")
PART_2_SAMPLE_INPUT = get_full_text("samples/part_2_input.txt")
PART_2_SAMPLE_SOLUTION = get_full_text("samples/part_2_solution.txt")


def test_part_1_solution():
    assert part_1_solution(PART_1_SAMPLE_INPUT) == PART_1_SAMPLE_SOLUTION


def test_part_2_solution():
    assert part_2_solution(PART_2_SAMPLE_INPUT) == PART_2_SAMPLE_SOLUTION


def part_1_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input,)
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
    pytest.main()
