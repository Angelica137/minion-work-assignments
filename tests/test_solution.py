from scripts.solution import solution

import random


def test_solution_1():
    assert solution([1, 2, 3], 0) == []


def test_solution_2():
    assert solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1, 4]


def test_solution_3():
    assert solution([5, 10, 15, 10, 7], 1) == [5, 15, 7]


def test_solution_4():
    assert solution([1, 2, 3], 6) == [1, 2, 3]


def test_solution_5():
    assert solution([], 6) == []


def test_more_than_99():
    data = []
    for i in range(0, 100):
        n = random.randint(1, 100)
        data.append(n)
    assert solution(data, 1) == None
