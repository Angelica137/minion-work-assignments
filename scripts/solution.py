import random


def solution(data: list, n: int) -> list:
    """
    Removes the items that repeat more times than :param: n
    from :param: data
    :returns: the updated list
    """
    print(len(data))
    if len(data) == 100:
        print("I have more than 100 items")
    """
    if len(data) < 5:
        for item in data:
            if data.count(item) > n:
                data = [x for x in data if x != item]
        return data
    """


data = []
for i in range(0, 100):
    n = random.randint(1, 100)
    data.append(n)

print(len(data))

print(solution(data, 1))
