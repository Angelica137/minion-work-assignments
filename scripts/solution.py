def solution(data: list, n: int) -> list:
    """
    Removes the items that repeat more times than :param: n
    from :param: data
    :returns: the updated list
    """
    count = {}
    for item in data:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    new_tasks = []
    for key in count:
        if count[key] <= n:
            new_tasks.append(key)
    return new_tasks


def solution_string(data, n) -> str:
    tasks = []
    output_string = ''
    for i in data:
        if i not in tasks and data.count(i) <= n and n > 0:
            tasks.append(str(i))
            tasks.append(',')
    for i in tasks:
        output_string += i
    return output_string[:-1]
