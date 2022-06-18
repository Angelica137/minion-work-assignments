def solution(data: list, n: int) -> list:
    """
    Removes the items that are greater than :param: n
    from :param: data
    :returns: the updated list
    """
    count = 0
    jobs = []
    for i in data:
        if (i + 1) == i:
            count += 1
        if count < n:
            jobs.append(i)
