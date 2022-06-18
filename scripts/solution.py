def solution(data: list, n: int) -> list:
    """
    Removes the items that are greater than :param: n
    from :param: data
    :returns: the updated list
    """
    for item in data:
        if data.count(item) > n:
            data = [x for x in data if x != item]
    return data
