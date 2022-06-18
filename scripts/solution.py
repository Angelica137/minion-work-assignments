def solution(data: list, n: int) -> list:
    """
    Removes the items that are greater than :param: n
    from :param: data
    :returns: the updated list
    """
    for item in data:
        count = data.count(item)
        print(count)
        if count > n:
            data = [x for x in data if x != item]
        item += 1
    return data


print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
