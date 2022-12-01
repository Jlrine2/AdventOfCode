from solution import silver_solution, gold_solution, INPUT


def pytest_unconfigure():
    print(f"Silver Solution: {silver_solution(INPUT)}")
    print(f"Gold Solution: {gold_solution(INPUT)}")
