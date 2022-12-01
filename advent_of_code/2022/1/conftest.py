from solution import part_1_solution, part_2_solution, INPUT


def pytest_unconfigure():
    print(f"Part 1 Solution: {part_1_solution(INPUT)}")
    print(f"Part 2 Solution: {part_2_solution(INPUT)}")
