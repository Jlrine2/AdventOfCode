import pytest

from helpers import *
from helpers import get_full_text

SILVER_SAMPLE_INPUT = get_full_text("silver/sample_input.txt")
SILVER_SAMPLE_OUTPUT = get_full_text("silver/sample_output.txt")

GOLD_SAMPLE_INPUT = get_full_text("gold/sample_input.txt")
GOLD_SAMPLE_OUTPUT = get_full_text("gold/sample_output.txt")

INPUT = get_full_text("input.txt")


def test_silver_solution():
    assert silver_solution(SILVER_SAMPLE_INPUT) == SILVER_SAMPLE_OUTPUT


def test_gold_solution():
    assert gold_solution(GOLD_SAMPLE_INPUT) == GOLD_SAMPLE_OUTPUT


def silver_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input)

    # Solution code goes here
    return ''


def gold_solution(puzzle_input):
    lines = full_text_to_list(puzzle_input)

    # Solution code goes here
    return ''


if __name__ == "__main__":
    pytest.main()
