from scripts.solution import solution


def test_solution_1():
    assert solution([1, 2, 3], 0) == []


def test_solution_2():
    assert solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1, 4]
